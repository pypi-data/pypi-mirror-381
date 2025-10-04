from fastmcp import FastMCP
from datetime import datetime
from typing import List
from fastmcp.server.middleware import Middleware, MiddlewareContext
from fastmcp import Context
from fastmcp.server.dependencies import get_http_request
from starlette.requests import Request


flowlens_mcp = FastMCP("Flowlens Map", stateless_http=True)


class UserAuthMiddleware(Middleware):
    async def on_call_tool(self, context: MiddlewareContext, call_next):
        request: Request = get_http_request()
        auth_header = request.headers.get("Authorization")
        
        if not auth_header:
            raise Exception("Authorization header missing")
        
        token = auth_header.split(" ")[1]
        print(f"Extracted Token: {token}")
        return await call_next(context=context)
        
flowlens_mcp.add_middleware(UserAuthMiddleware())
        

@flowlens_mcp.tool
def get_current_datetime_iso_format() -> str:
    return datetime.utcnow().isoformat()


@flowlens_mcp.tool
async def list_flows(ctx: Context) -> List[dict]:
    """
    List all flows for the authenticated user.
    Args:
        data: Input data (not used)
    Returns:
        List of Flow dictionaries    
    """
    flows = []
    for i, flow in enumerate(await ctx.get_flows()):
        dummy_flow = {
            "id": flow.id,
            "name": f"Flow {i+1}",
            "description": f"Description for Flow {i+1}",
            "created_at": flow.created_at,
            "updated_at": flow.updated_at,
        }
        flows.append(dummy_flow)
    return flows


def main():
    flowlens_mcp.run(transport="http", path="/mcp_stream/mcp/")
    
if __name__ == "__main__":
    main()
