#!/usr/bin/env python3
"""
Math MCP Server - FastMCP 2.0 Implementation
Educational MCP server demonstrating all three MCP pillars: Tools, Resources, and Prompts.
Uses FastMCP 2.0 patterns with structured output and multi-transport support.
"""

import logging
import math
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field
from fastmcp import FastMCP, Context


# === PYDANTIC MODELS FOR STRUCTURED OUTPUT ===

class CalculationResult(BaseModel):
    """Structured result for mathematical calculations."""
    expression: str = Field(description="The original expression")
    result: float = Field(description="The calculated result")
    timestamp: str = Field(description="When the calculation was performed")


class StatisticsResult(BaseModel):
    """Structured result for statistical calculations."""
    operation: str = Field(description="Statistical operation performed")
    input_data: list[float] = Field(description="Input numbers")
    result: float = Field(description="Statistical result")
    count: int = Field(description="Number of data points")


class CompoundInterestResult(BaseModel):
    """Structured result for compound interest calculations."""
    principal: float = Field(description="Initial investment")
    rate: float = Field(description="Annual interest rate")
    time: float = Field(description="Investment period in years")
    compounds_per_year: int = Field(description="Compounding frequency")
    final_amount: float = Field(description="Final amount after compound interest")
    total_interest: float = Field(description="Total interest earned")


class UnitConversionResult(BaseModel):
    """Structured result for unit conversions."""
    original_value: float = Field(description="Original value")
    original_unit: str = Field(description="Original unit")
    converted_value: float = Field(description="Converted value")
    target_unit: str = Field(description="Target unit")
    conversion_type: str = Field(description="Type of conversion")


# === APPLICATION CONTEXT ===

@dataclass
class AppContext:
    """Application context with calculation history."""
    calculation_history: list[dict[str, Any]]


@asynccontextmanager
async def app_lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    """Manage application lifecycle with calculation history."""
    # Initialize calculation history
    calculation_history: list[dict[str, Any]] = []
    try:
        yield AppContext(calculation_history=calculation_history)
    finally:
        # Could save history to file here
        pass


# === FASTMCP SERVER SETUP ===

mcp = FastMCP(
    name="Math Learning Server",
    lifespan=app_lifespan,
    instructions="A comprehensive math server demonstrating MCP fundamentals with tools, resources, and prompts for educational purposes."
)


# === SECURITY: SAFE EXPRESSION EVALUATION ===

def _validate_expression_syntax(expression: str) -> None:
    """Provide specific error messages for common syntax errors."""
    clean_expr = expression.replace(" ", "").lower()

    # Check for common function syntax issues
    if "pow(" in clean_expr and "," not in clean_expr:
        raise ValueError("Function 'pow()' requires two parameters: pow(base, exponent). Example: pow(2, 3)")

    # Check for empty function calls (functions with no parameters)
    single_param_funcs = ["sin", "cos", "tan", "log", "sqrt", "abs"]
    for func in single_param_funcs:
        empty_call = f"{func}()"
        if empty_call in clean_expr:
            raise ValueError(f"Function '{func}()' requires one parameter. Example: {func}(3.14)")

def safe_eval_expression(expression: str) -> float:
    """Safely evaluate mathematical expressions with restricted scope."""
    # Validate syntax and provide helpful error messages
    _validate_expression_syntax(expression)

    # Remove whitespace
    clean_expr = expression.replace(" ", "")

    # Only allow safe characters (including comma for function parameters)
    allowed_chars = set("0123456789+-*/.(),e")
    allowed_functions = {"sin", "cos", "tan", "log", "sqrt", "abs", "pow"}

    # Security check - log and block dangerous patterns
    dangerous_patterns = ["import", "exec", "__", "eval", "open", "file"]
    if any(pattern in clean_expr.lower() for pattern in dangerous_patterns):
        logging.warning(f"Security: Blocked unsafe expression attempt: {expression[:50]}...")
        raise ValueError("Expression contains forbidden operations. Only mathematical expressions are allowed.")

    # Check for unsafe characters
    if not all(c in allowed_chars or c.isalpha() for c in clean_expr):
        raise ValueError("Expression contains invalid characters. Use only numbers, +, -, *, /, (), and math functions.")

    # Replace math functions with safe alternatives
    safe_expr = clean_expr
    for func in allowed_functions:
        if func in clean_expr:
            if func != "abs":  # abs is built-in, others need math module
                safe_expr = safe_expr.replace(func, f"math.{func}")

    # Evaluate with restricted globals
    try:
        allowed_globals = {"__builtins__": {"abs": abs}, "math": math}
        result = eval(safe_expr, allowed_globals, {})
        return float(result)
    except ZeroDivisionError:
        raise ValueError("Mathematical error: Division by zero is undefined.")
    except OverflowError:
        raise ValueError("Mathematical error: Result is too large to compute.")
    except ValueError as e:
        if "math domain error" in str(e):
            raise ValueError("Mathematical error: Invalid input for function (e.g., sqrt of negative number).")
        raise ValueError(f"Mathematical expression error: {str(e)}")
    except Exception as e:
        raise ValueError(f"Expression evaluation failed: {str(e)}")


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """Convert temperature between Celsius, Fahrenheit, and Kelvin."""
    # Convert to Celsius first
    if from_unit.lower() == "f":
        celsius = (value - 32) * 5/9
    elif from_unit.lower() == "k":
        celsius = value - 273.15
    else:  # Celsius
        celsius = value

    # Convert from Celsius to target
    if to_unit.lower() == "f":
        return celsius * 9/5 + 32
    elif to_unit.lower() == "k":
        return celsius + 273.15
    else:  # Celsius
        return celsius


# === TOOLS: COMPUTATIONAL OPERATIONS ===

def _classify_expression_difficulty(expression: str) -> str:
    """Classify mathematical expression difficulty for educational annotations."""
    clean_expr = expression.replace(" ", "").lower()

    # Count complexity indicators
    has_functions = any(func in clean_expr for func in ["sin", "cos", "tan", "log", "sqrt", "pow"])
    has_parentheses = "(" in clean_expr
    has_exponents = "**" in clean_expr or "^" in clean_expr
    operator_count = sum(clean_expr.count(op) for op in "+-*/")

    if has_functions or has_exponents:
        return "advanced"
    elif has_parentheses or operator_count > 2:
        return "intermediate"
    else:
        return "basic"


def _classify_expression_topic(expression: str) -> str:
    """Enhanced topic classification for educational metadata."""
    clean_expr = expression.lower()

    if any(word in clean_expr for word in ["interest", "rate", "investment", "portfolio"]):
        return "finance"
    elif any(word in clean_expr for word in ["pi", "radius", "area", "volume"]):
        return "geometry"
    elif any(word in clean_expr for word in ["sin", "cos", "tan"]):
        return "trigonometry"
    elif any(word in clean_expr for word in ["log", "ln", "exp"]):
        return "logarithms"
    else:
        return "arithmetic"

@mcp.tool(
    annotations={
        "title": "Mathematical Calculator",
        "readOnlyHint": False,
        "openWorldHint": True
    }
)
async def calculate(
    expression: str,
    ctx: Context
) -> dict[str, Any]:
    """Safely evaluate mathematical expressions with support for basic operations and math functions.

    Supported operations: +, -, *, /, **, ()
    Supported functions: sin, cos, tan, log, sqrt, abs, pow

    Examples:
    - "2 + 3 * 4" → 14
    - "sqrt(16)" → 4.0
    - "sin(3.14159/2)" → 1.0
    """
    # FastMCP 2.0 Context logging best practice
    await ctx.info(f"Calculating expression: {expression}")

    result = safe_eval_expression(expression)
    timestamp = datetime.now().isoformat()
    difficulty = _classify_expression_difficulty(expression)

    # Add to calculation history
    history_entry = {
        "type": "calculation",
        "expression": expression,
        "result": result,
        "timestamp": timestamp
    }
    ctx.request_context.lifespan_context.calculation_history.append(history_entry)

    # Return content with educational annotations
    return {
        "content": [
            {
                "type": "text",
                "text": f"**Calculation:** {expression} = {result}",
                "annotations": {
                    "difficulty": difficulty,
                    "topic": "arithmetic",
                    "timestamp": timestamp
                }
            }
        ]
    }


@mcp.tool(
    annotations={
        "title": "Statistical Analysis",
        "readOnlyHint": True,
        "openWorldHint": False
    }
)
async def statistics(
    numbers: list[float],
    operation: str,
    ctx: Context
) -> dict[str, Any]:
    """Perform statistical calculations on a list of numbers.

    Available operations: mean, median, mode, std_dev, variance
    """
    # FastMCP 2.0 Context logging - demonstrates async operation with user feedback
    await ctx.info(f"Performing {operation} on {len(numbers)} data points")

    import statistics as stats  # Import with alias to avoid naming conflict

    if not numbers:
        raise ValueError("Cannot calculate statistics on empty list")

    operations = {
        "mean": stats.mean,
        "median": stats.median,
        "mode": stats.mode,
        "std_dev": lambda x: stats.stdev(x) if len(x) > 1 else 0,
        "variance": lambda x: stats.variance(x) if len(x) > 1 else 0
    }

    if operation not in operations:
        raise ValueError(f"Unknown operation '{operation}'. Available: {list(operations.keys())}")

    result = operations[operation](numbers)
    # Ensure result is always a float for type safety
    # Since input is list[float], all results should be convertible to float
    result_float = float(result)  # type: ignore[arg-type]

    # Determine difficulty based on operation and data size
    difficulty = "advanced" if operation in ["std_dev", "variance"] else "intermediate" if len(numbers) > 10 else "basic"

    return {
        "content": [
            {
                "type": "text",
                "text": f"**{operation.title()}** of {len(numbers)} numbers: {result_float}",
                "annotations": {
                    "difficulty": difficulty,
                    "topic": "statistics",
                    "operation": operation,
                    "sample_size": len(numbers)
                }
            }
        ]
    }


@mcp.tool()
async def compound_interest(
    principal: float,
    rate: float,
    time: float,
    compounds_per_year: int = 1,
    ctx: Context = None  # type: ignore[assignment]
) -> dict[str, Any]:
    """Calculate compound interest for investments.

    Formula: A = P(1 + r/n)^(nt)
    Where:
    - P = principal amount
    - r = annual interest rate (as decimal)
    - n = number of times interest compounds per year
    - t = time in years
    """
    # FastMCP 2.0 Context logging - provides visibility into financial calculations
    if ctx:
        await ctx.info(f"Calculating compound interest: ${principal:,.2f} @ {rate*100}% for {time} years")

    if principal <= 0:
        raise ValueError("Principal must be greater than 0")
    if rate < 0:
        raise ValueError("Interest rate cannot be negative")
    if time <= 0:
        raise ValueError("Time must be greater than 0")
    if compounds_per_year <= 0:
        raise ValueError("Compounds per year must be greater than 0")

    # Calculate compound interest: A = P(1 + r/n)^(nt)
    final_amount = principal * (1 + rate / compounds_per_year) ** (compounds_per_year * time)
    total_interest = final_amount - principal

    return {
        "content": [
            {
                "type": "text",
                "text": f"**Compound Interest Calculation:**\nPrincipal: ${principal:,.2f}\nFinal Amount: ${final_amount:,.2f}\nTotal Interest Earned: ${total_interest:,.2f}",
                "annotations": {
                    "difficulty": "intermediate",
                    "topic": "finance",
                    "formula": "A = P(1 + r/n)^(nt)",
                    "time_years": time
                }
            }
        ]
    }


@mcp.tool()
async def convert_units(
    value: float,
    from_unit: str,
    to_unit: str,
    unit_type: str,
    ctx: Context = None  # type: ignore[assignment]
) -> dict[str, Any]:
    """Convert between different units of measurement.

    Supported unit types:
    - length: mm, cm, m, km, in, ft, yd, mi
    - weight: g, kg, oz, lb
    - temperature: c, f, k (Celsius, Fahrenheit, Kelvin)
    """
    # FastMCP 2.0 Context logging - tracks conversion operations for educational purposes
    if ctx:
        await ctx.info(f"Converting {value} {from_unit} to {to_unit} ({unit_type})")

    # Conversion tables (to base units)
    conversions = {
        "length": {  # to millimeters
            "mm": 1, "cm": 10, "m": 1000, "km": 1000000,
            "in": 25.4, "ft": 304.8, "yd": 914.4, "mi": 1609344
        },
        "weight": {  # to grams
            "g": 1, "kg": 1000, "oz": 28.35, "lb": 453.59
        }
    }

    if unit_type == "temperature":
        result = convert_temperature(value, from_unit, to_unit)
    else:
        conversion_table = conversions.get(unit_type)
        if not conversion_table:
            raise ValueError(f"Unknown unit type '{unit_type}'. Available: length, weight, temperature")

        from_factor = conversion_table.get(from_unit.lower())
        to_factor = conversion_table.get(to_unit.lower())

        if from_factor is None:
            raise ValueError(f"Unknown {unit_type} unit '{from_unit}'")
        if to_factor is None:
            raise ValueError(f"Unknown {unit_type} unit '{to_unit}'")

        # Convert: value → base unit → target unit
        base_value = value * from_factor
        result = base_value / to_factor

    return {
        "content": [
            {
                "type": "text",
                "text": f"**Unit Conversion:** {value} {from_unit} = {result:.4g} {to_unit}",
                "annotations": {
                    "difficulty": "basic",
                    "topic": "unit_conversion",
                    "conversion_type": unit_type,
                    "from_unit": from_unit,
                    "to_unit": to_unit
                }
            }
        ]
    }


@mcp.tool(
    annotations={
        "title": "Save Calculation to Workspace",
        "readOnlyHint": False,
        "openWorldHint": False
    }
)
async def save_calculation(
    name: str,
    expression: str,
    result: float,
    ctx: Context
) -> dict[str, Any]:
    """Save calculation to persistent workspace (survives restarts).

    Args:
        name: Variable name to save under
        expression: The mathematical expression
        result: The calculated result

    Examples:
        save_calculation("portfolio_return", "10000 * 1.07^5", 14025.52)
        save_calculation("circle_area", "pi * 5^2", 78.54)
    """
    # FastMCP 2.0 Context logging
    await ctx.info(f"Saving calculation '{name}' = {result}")
    # Validate inputs
    if not name.strip():
        raise ValueError("Variable name cannot be empty")

    if not name.replace('_', '').replace('-', '').isalnum():
        raise ValueError("Variable name must contain only letters, numbers, underscores, and hyphens")

    # Get educational metadata from expression classification
    difficulty = _classify_expression_difficulty(expression)
    topic = _classify_expression_topic(expression)

    metadata = {
        "difficulty": difficulty,
        "topic": topic,
        "session_id": id(ctx.request_context.lifespan_context)
    }

    # Save to persistent workspace
    from math_mcp.persistence.workspace import _workspace_manager
    result_data = _workspace_manager.save_variable(name, expression, result, metadata)

    # Also add to session history
    history_entry = {
        "type": "save_calculation",
        "name": name,
        "expression": expression,
        "result": result,
        "timestamp": datetime.now().isoformat()
    }
    ctx.request_context.lifespan_context.calculation_history.append(history_entry)

    return {
        "content": [
            {
                "type": "text",
                "text": f"**Saved Variable:** {name} = {result}\n**Expression:** {expression}\n**Status:** {'Success' if result_data['success'] else 'Failed'}",
                "annotations": {
                    "action": "save_calculation",
                    "variable_name": name,
                    "is_new": result_data.get("is_new", True),
                    "total_variables": result_data.get("total_variables", 0),
                    **metadata
                }
            }
        ]
    }


@mcp.tool()
async def load_variable(
    name: str,
    ctx: Context
) -> dict[str, Any]:
    """Load previously saved calculation result from workspace.

    Args:
        name: Variable name to load

    Examples:
        load_variable("portfolio_return")  # Returns saved calculation
        load_variable("circle_area")       # Access across sessions
    """
    # FastMCP 2.0 Context logging
    await ctx.info(f"Loading variable '{name}'")
    from math_mcp.persistence.workspace import _workspace_manager
    result_data = _workspace_manager.load_variable(name)

    if not result_data["success"]:
        available = result_data.get("available_variables", [])
        error_msg = result_data["error"]
        if available:
            error_msg += f"\nAvailable variables: {', '.join(available)}"

        return {
            "content": [
                {
                    "type": "text",
                    "text": f"**Error:** {error_msg}",
                    "annotations": {
                        "action": "load_variable_error",
                        "requested_name": name,
                        "available_count": len(available)
                    }
                }
            ]
        }

    # Add to session history
    history_entry = {
        "type": "load_variable",
        "name": name,
        "expression": result_data["expression"],
        "result": result_data["result"],
        "timestamp": datetime.now().isoformat()
    }
    ctx.request_context.lifespan_context.calculation_history.append(history_entry)

    return {
        "content": [
            {
                "type": "text",
                "text": f"**Loaded Variable:** {name} = {result_data['result']}\n**Expression:** {result_data['expression']}\n**Saved:** {result_data['timestamp']}",
                "annotations": {
                    "action": "load_variable",
                    "variable_name": name,
                    "original_timestamp": result_data["timestamp"],
                    **result_data.get("metadata", {})
                }
            }
        ]
    }


@mcp.tool(
    annotations={
        "title": "Function Plotter",
        "readOnlyHint": False,
        "openWorldHint": False
    }
)
async def plot_function(
    expression: str,
    x_range: tuple[float, float],
    num_points: int = 100,
    ctx: Context | None = None
) -> dict[str, Any]:
    """Generate mathematical function plots (requires matplotlib).

    Args:
        expression: Mathematical expression to plot (e.g., "x**2", "sin(x)")
        x_range: Tuple of (min, max) for x-axis range
        num_points: Number of points to plot (default: 100)
        ctx: FastMCP context for logging

    Returns:
        Dict with base64-encoded PNG image or error message

    Examples:
        plot_function("x**2", (-5, 5))
        plot_function("sin(x)", (-3.14, 3.14))
    """
    # Try importing optional dependencies
    try:
        import matplotlib
        matplotlib.use('Agg')  # Non-interactive backend
        import matplotlib.pyplot as plt
        import numpy as np
    except ImportError:
        return {
            "content": [{
                "type": "text",
                "text": "**Matplotlib not available**\n\nInstall with: `pip install math-mcp-learning-server[plotting]`\n\nOr for development: `uv sync --extra plotting`",
                "annotations": {
                    "error": "missing_dependency",
                    "install_command": "pip install math-mcp-learning-server[plotting]",
                    "difficulty": "intermediate",
                    "topic": "visualization"
                }
            }]
        }

    # FastMCP 2.0 Context logging
    if ctx:
        await ctx.info(f"Plotting function: {expression} over range {x_range}")

    try:
        # Validate x_range
        x_min, x_max = x_range
        if x_min >= x_max:
            raise ValueError("x_range minimum must be less than maximum")
        if num_points < 2:
            raise ValueError("num_points must be at least 2")

        # Generate x values
        x_values = np.linspace(x_min, x_max, num_points)

        # Evaluate expression for each x value
        y_values = []
        for x in x_values:
            # Replace x in expression with actual value
            expr_with_value = expression.replace('x', f'({x})')
            try:
                y = safe_eval_expression(expr_with_value)
                y_values.append(y)
            except ValueError:
                # Handle domain errors (like sqrt of negative)
                y_values.append(float('nan'))

        # Create figure and plot
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(x_values, y_values, linewidth=2, color='#2E86AB')
        ax.set_xlabel('x', fontsize=12)
        ax.set_ylabel('f(x)', fontsize=12)
        ax.set_title(f'Plot of f(x) = {expression}', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.axhline(y=0, color='k', linewidth=0.5)
        ax.axvline(x=0, color='k', linewidth=0.5)

        # Save to base64
        from io import BytesIO
        import base64

        buffer = BytesIO()
        plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
        plt.close(fig)
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.read()).decode('utf-8')

        # Classify difficulty
        difficulty = _classify_expression_difficulty(expression)

        return {
            "content": [{
                "type": "image",
                "data": image_base64,
                "mimeType": "image/png",
                "annotations": {
                    "difficulty": difficulty,
                    "topic": "visualization",
                    "expression": expression,
                    "x_range": f"[{x_min}, {x_max}]",
                    "num_points": num_points,
                    "educational_note": "Function plotting visualizes mathematical relationships"
                }
            }]
        }

    except ValueError as e:
        return {
            "content": [{
                "type": "text",
                "text": f"**Plot Error:** {str(e)}\n\nPlease check your expression and x_range values.",
                "annotations": {
                    "error": "plot_error",
                    "difficulty": "intermediate",
                    "topic": "visualization"
                }
            }]
        }
    except Exception as e:
        return {
            "content": [{
                "type": "text",
                "text": f"**Unexpected Error:** {str(e)}",
                "annotations": {
                    "error": "unexpected_error",
                    "difficulty": "intermediate",
                    "topic": "visualization"
                }
            }]
        }


@mcp.tool(
    annotations={
        "title": "Statistical Histogram",
        "readOnlyHint": False,
        "openWorldHint": False
    }
)
async def create_histogram(
    data: list[float],
    bins: int = 20,
    title: str = "Data Distribution",
    ctx: Context | None = None
) -> dict[str, Any]:
    """Create statistical histograms (requires matplotlib).

    Args:
        data: List of numerical values
        bins: Number of histogram bins (default: 20)
        title: Chart title
        ctx: FastMCP context for logging

    Returns:
        Dict with base64-encoded PNG image or error message

    Examples:
        create_histogram([1, 2, 2, 3, 3, 3, 4, 4, 5], bins=5)
    """
    # Try importing optional dependencies
    try:
        import matplotlib
        matplotlib.use('Agg')  # Non-interactive backend
        import matplotlib.pyplot as plt
        import numpy  # noqa: F401 - imported for side effects, required by matplotlib
    except ImportError:
        return {
            "content": [{
                "type": "text",
                "text": "**Matplotlib not available**\n\nInstall with: `pip install math-mcp-learning-server[plotting]`\n\nOr for development: `uv sync --extra plotting`",
                "annotations": {
                    "error": "missing_dependency",
                    "install_command": "pip install math-mcp-learning-server[plotting]",
                    "difficulty": "intermediate",
                    "topic": "visualization"
                }
            }]
        }

    # FastMCP 2.0 Context logging
    if ctx:
        await ctx.info(f"Creating histogram with {len(data)} data points and {bins} bins")

    try:
        # Validate inputs
        if not data:
            raise ValueError("Cannot create histogram with empty data")
        if len(data) == 1:
            raise ValueError("Histogram requires at least 2 data points")
        if bins < 1:
            raise ValueError("bins must be at least 1")

        # Calculate statistics
        import statistics as stats
        mean_val = stats.mean(data)
        median_val = stats.median(data)
        std_dev = stats.stdev(data) if len(data) > 1 else 0

        # Create histogram
        fig, ax = plt.subplots(figsize=(10, 6))
        n, bins_edges, patches = ax.hist(data, bins=bins, color='#A23B72', alpha=0.7, edgecolor='black')

        # Add vertical lines for mean and median
        ax.axvline(mean_val, color='#F18F01', linestyle='--', linewidth=2, label=f'Mean: {mean_val:.2f}')
        ax.axvline(median_val, color='#C73E1D', linestyle='-.', linewidth=2, label=f'Median: {median_val:.2f}')

        ax.set_xlabel('Value', fontsize=12)
        ax.set_ylabel('Frequency', fontsize=12)
        ax.set_title(title, fontsize=14, fontweight='bold')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')

        # Save to base64
        from io import BytesIO
        import base64

        buffer = BytesIO()
        plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
        plt.close(fig)
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.read()).decode('utf-8')

        return {
            "content": [{
                "type": "image",
                "data": image_base64,
                "mimeType": "image/png",
                "annotations": {
                    "difficulty": "intermediate",
                    "topic": "statistics",
                    "data_points": len(data),
                    "bins": bins,
                    "mean": round(mean_val, 4),
                    "median": round(median_val, 4),
                    "std_dev": round(std_dev, 4),
                    "educational_note": "Histograms show the distribution and frequency of data values"
                }
            }]
        }

    except ValueError as e:
        return {
            "content": [{
                "type": "text",
                "text": f"**Histogram Error:** {str(e)}\n\nPlease check your data and parameters.",
                "annotations": {
                    "error": "histogram_error",
                    "difficulty": "intermediate",
                    "topic": "visualization"
                }
            }]
        }
    except Exception as e:
        return {
            "content": [{
                "type": "text",
                "text": f"**Unexpected Error:** {str(e)}",
                "annotations": {
                    "error": "unexpected_error",
                    "difficulty": "intermediate",
                    "topic": "visualization"
                }
            }]
        }


# === RESOURCES: DATA EXPOSURE ===

@mcp.resource("math://test")
async def simple_test(ctx: Context) -> str:
    """Simple test resource like FastMCP examples"""
    await ctx.info("Accessing test resource")
    return "Test resource working successfully!"

@mcp.resource(
    "math://constants/{constant}",
    annotations={
        "readOnlyHint": True,
        "idempotentHint": True
    }
)
def get_math_constant(constant: str) -> str:
    """Get mathematical constants like pi, e, golden ratio, etc."""
    constants = {
        "pi": {"value": math.pi, "description": "Ratio of circle's circumference to diameter"},
        "e": {"value": math.e, "description": "Euler's number, base of natural logarithm"},
        "golden_ratio": {"value": (1 + math.sqrt(5)) / 2, "description": "Golden ratio φ"},
        "euler_gamma": {"value": 0.5772156649015329, "description": "Euler-Mascheroni constant γ"},
        "sqrt2": {"value": math.sqrt(2), "description": "Square root of 2"},
        "sqrt3": {"value": math.sqrt(3), "description": "Square root of 3"}
    }

    if constant not in constants:
        available = ", ".join(constants.keys())
        return f"Unknown constant '{constant}'. Available constants: {available}"

    const_info = constants[constant]
    return f"{constant}: {const_info['value']}\nDescription: {const_info['description']}"


@mcp.resource("math://functions")
async def list_available_functions(ctx: Context) -> str:
    """List all available mathematical functions with examples and syntax help."""
    await ctx.info("Accessing function reference documentation")
    return """# Available Mathematical Functions

## Basic Functions
- **abs(x)**: Absolute value
  - Example: abs(-5) = 5.0

## Trigonometric Functions
- **sin(x)**: Sine (input in radians)
  - Example: sin(3.14159/2) ≈ 1.0
- **cos(x)**: Cosine (input in radians)
  - Example: cos(0) = 1.0
- **tan(x)**: Tangent (input in radians)
  - Example: tan(3.14159/4) ≈ 1.0

## Mathematical Functions
- **sqrt(x)**: Square root
  - Example: sqrt(16) = 4.0
- **log(x)**: Natural logarithm
  - Example: log(2.71828) ≈ 1.0
- **pow(x, y)**: x raised to the power of y
  - Example: pow(2, 3) = 8.0

## Usage Notes
- All functions use parentheses: function(parameter)
- Multi-parameter functions use commas: pow(base, exponent)
- Use operators for basic math: +, -, *, /, **
- Parentheses for grouping: (2 + 3) * 4

## Examples
- Simple: 2 + 3 * 4 = 14.0
- Functions: sqrt(16) + pow(2, 3) = 12.0
- Complex: sin(3.14159/2) + cos(0) = 2.0
"""


@mcp.resource("math://history")
async def get_calculation_history(ctx: Context) -> str:
    """Get the history of calculations performed across sessions."""
    await ctx.info("Accessing calculation history")
    from math_mcp.persistence.workspace import _workspace_manager

    # Get workspace history
    workspace_data = _workspace_manager._load_workspace()

    if not workspace_data.variables:
        return "No calculations in workspace yet. Use save_calculation() to persist calculations."

    history_text = "Calculation History (from workspace):\n\n"

    # Sort by timestamp to show chronological order
    variables = list(workspace_data.variables.items())
    variables.sort(key=lambda x: x[1].timestamp, reverse=True)

    for i, (name, var) in enumerate(variables[:10], 1):  # Show last 10
        history_text += f"{i}. {name}: {var.expression} = {var.result} (saved {var.timestamp})\n"

    if len(variables) > 10:
        history_text += f"\n... and {len(variables) - 10} more calculations"

    return history_text


@mcp.resource(
    "math://workspace",
    annotations={
        "readOnlyHint": True,
        "idempotentHint": False
    }
)
async def get_workspace(ctx: Context) -> str:
    """Get persistent calculation workspace showing all saved variables.

    This resource displays the complete state of the persistent workspace,
    including all saved calculations, metadata, and statistics. The workspace
    survives server restarts and is accessible across different transport modes.
    """
    await ctx.info("Accessing persistent workspace")
    from math_mcp.persistence.workspace import _workspace_manager
    return _workspace_manager.get_workspace_summary()


# === PROMPTS: INTERACTION TEMPLATES ===

@mcp.prompt()
def math_tutor(
    topic: str,
    level: str = "intermediate",
    include_examples: bool = True
) -> str:
    """Generate a math tutoring prompt for explaining concepts.

    Args:
        topic: Mathematical topic to explain (e.g., "derivatives", "statistics")
        level: Difficulty level (beginner, intermediate, advanced)
        include_examples: Whether to include worked examples
    """
    prompt = f"""You are an expert mathematics tutor. Please explain the concept of {topic} at a {level} level.

Please structure your explanation as follows:
1. **Definition**: Provide a clear, concise definition
2. **Key Concepts**: Break down the main ideas
3. **Applications**: Where this is used in real life
"""

    if include_examples:
        prompt += "4. **Worked Examples**: Provide 2-3 step-by-step examples\n"

    prompt += f"""
Make your explanation engaging and accessible for a {level} learner. Use analogies when helpful, and encourage questions.
"""

    return prompt


@mcp.prompt()
def formula_explainer(
    formula: str,
    context: str = "general mathematics"
) -> str:
    """Generate a prompt for explaining mathematical formulas in detail.

    Args:
        formula: The mathematical formula to explain (e.g., "A = πr²")
        context: The mathematical context (e.g., "geometry", "calculus", "statistics")
    """
    return f"""Please provide a comprehensive explanation of the formula: {formula}

Include the following in your explanation:

1. **What it represents**: What does this formula calculate or describe?
2. **Variable definitions**: Define each variable/symbol in the formula
3. **Context**: How this formula fits within {context}
4. **Step-by-step breakdown**: If the formula has multiple parts, explain each step
5. **Example calculation**: Show how to use the formula with specific numbers
6. **Real-world applications**: Where might someone use this formula?
7. **Common mistakes**: What errors do people often make when using this formula?

Make your explanation clear and educational, suitable for someone learning about {context}.
"""


# === MAIN ENTRY POINT ===

def main() -> None:
    """Main entry point supporting multiple transports."""
    import sys
    from typing import cast, Literal

    # Parse command line arguments for transport type
    transport: Literal["stdio", "sse", "streamable-http"] = "stdio"  # default
    if len(sys.argv) > 1:
        if sys.argv[1] in ["stdio", "sse", "streamable-http"]:
            transport = cast(Literal["stdio", "sse", "streamable-http"], sys.argv[1])

    # Run with specified transport
    mcp.run(transport=transport)


if __name__ == "__main__":
    main()