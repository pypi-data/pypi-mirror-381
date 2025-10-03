import logging
from inspect import Parameter, signature
from typing import Any, Callable, Dict, Optional, Type, Union

from mcp.types import Tool as MCPTool
from pydantic import BaseModel, Field, create_model

from dapr_agents.tool.utils.function_calling import validate_and_format_tool
from dapr_agents.types import ToolError
from dapr_agents.types.tools import GeminiFunctionDefinition, OAIFunctionDefinition

logger = logging.getLogger(__name__)


class ToolHelper:
    """
    Utility class for common operations related to agent tools, such as validating docstrings,
    formatting tools for specific APIs, and inferring Pydantic schemas from function signatures.
    """

    @staticmethod
    def check_docstring(func: Callable) -> None:
        """
        Ensures a function has a docstring, raising an error if missing.

        Args:
            func (Callable): The function to verify.

        Raises:
            ToolError: Raised if the function lacks a docstring.
        """
        if not func.__doc__:
            raise ToolError(
                f"Function '{func.__name__}' must have a docstring for documentation."
            )

    @staticmethod
    def format_tool(
        tool: Union[Dict[str, Any], Callable],
        tool_format: str = "openai",
        use_deprecated: bool = False,
    ) -> dict:
        """
        Validates and formats a tool for a specific API format.

        Args:
            tool (Union[Dict[str, Any], Callable]): The tool to format.
            tool_format (str): Format type, e.g., 'openai'.
            use_deprecated (bool): Set to use a deprecated format.

        Returns:
            dict: A formatted representation of the tool.
        """
        from dapr_agents.tool.base import AgentTool

        if callable(tool) and not isinstance(tool, AgentTool):
            tool = AgentTool.from_func(tool)
        elif isinstance(tool, dict):
            return validate_and_format_tool(tool, tool_format, use_deprecated)
        if not isinstance(tool, AgentTool):
            raise TypeError(f"Unsupported tool type: {type(tool).__name__}")
        # Treat 'dapr' like OpenAI-style function tools; Dapr client will convert
        fmt = tool_format if tool_format != "dapr" else "openai"
        return tool.to_function_call(format_type=fmt, use_deprecated=use_deprecated)

    @staticmethod
    def infer_func_schema(
        func: Callable, name: Optional[str] = None
    ) -> Type[BaseModel]:
        """
        Generates a Pydantic schema based on the function's signature and type hints.

        Args:
            func (Callable): The function from which to derive the schema.
            name (Optional[str]): An optional name for the generated Pydantic model.

        Returns:
            Type[BaseModel]: A Pydantic model representing the function's parameters.
        """
        sig = signature(func)
        fields = {}
        has_type_hints = False

        for name, param in sig.parameters.items():
            field_type = (
                param.annotation if param.annotation != Parameter.empty else str
            )
            has_type_hints = has_type_hints or param.annotation != Parameter.empty
            fields[name] = (
                field_type,
                Field(default=param.default)
                if param.default != Parameter.empty
                else Field(...),
            )

        model_name = name or f"{func.__name__}Model"
        if not has_type_hints:
            logger.warning(
                f"No type hints provided for function '{func.__name__}'. Defaulting to 'str'."
            )
        return (
            create_model(model_name, **fields)
            if fields
            else create_model(model_name, __base__=BaseModel)
        )

    @staticmethod
    def mcp_to_openai(mcp_tool: MCPTool) -> OAIFunctionDefinition:
        """
        Convert an MCPTool to an OAIFunctionDefinition (OpenAI format).

        Args:
            mcp_tool (MCPTool): The MCP tool object to convert.

        Returns:
            OAIFunctionDefinition: An OpenAI function definition object.
        """
        return OAIFunctionDefinition(
            name=mcp_tool.name,
            description=mcp_tool.description or "",
            parameters=getattr(mcp_tool, "inputSchema", {}) or {},
        )

    @staticmethod
    def mcp_to_gemini(mcp_tool: MCPTool) -> GeminiFunctionDefinition:
        """
        Convert an MCPTool to a GeminiFunctionDefinition (Gemini format).

        Args:
            mcp_tool (MCPTool): The MCP tool object to convert.

        Returns:
            GeminiFunctionDefinition: A Gemini function definition object.
        """
        return GeminiFunctionDefinition(
            name=mcp_tool.name,
            description=mcp_tool.description or "",
            parameters=getattr(mcp_tool, "inputSchema", {}) or {},
        )

    @staticmethod
    def mcp_tools_to_openai(mcp_tools: list) -> list:
        """
        Convert a list of MCPTool objects to OAIFunctionDefinition list.

        Args:
            mcp_tools (List[MCPTool]): List of MCP tool objects to convert.

        Returns:
            List[OAIFunctionDefinition]: List of OpenAI function definition objects.
        """
        return [ToolHelper.mcp_to_openai(tool) for tool in mcp_tools]

    @staticmethod
    def mcp_tools_to_gemini(mcp_tools: list) -> list:
        """
        Convert a list of MCPTool objects to GeminiFunctionDefinition list.

        Args:
            mcp_tools (List[MCPTool]): List of MCP tool objects to convert.

        Returns:
            List[GeminiFunctionDefinition]: List of Gemini function definition objects.
        """
        return [ToolHelper.mcp_to_gemini(tool) for tool in mcp_tools]
