from loguru import logger
from universal_mcp.integrations import integration
from universal_mcp.applications.yahoo_finance.app import YahooFinanceApp
from universal_mcp.applications.domain_checker import DomainCheckerApp
from universal_mcp.integrations.integration import Integration
from universal_mcp.applications.youtube.app import YoutubeApp
from universal_mcp.applications.scraper.app import ScraperApp
from universal_mcp.applications.hashnode.app import HashnodeApp
from universal_mcp.applications.browser_use.app import BrowserUseApp
from universal_mcp.integrations.integration import ApiKeyIntegration
import asyncio
 

async def main():
    # Method 1: Basic integration with credentials
    # integration = Integration(name="youtube")
    # integration.set_credentials({"api_key": "a01ae4d7-1bbb-4cbb-ab26-b27c19fd2756"})
    # integration = ApiKeyIntegration(name="browser_use")
    # Method 2: API Key integration (recommended)
    # from universal_mcp.integrations.integration import ApiKeyIntegration
    integration = ApiKeyIntegration(name="browser_use")
    integration.api_key = "bu_k_25g_9-yBxELx9lb-gGyQ_KmIpBuBlcJ-LZ-QcEcJE"
    
    # app = HashnodeApp(integration=integration)
    app = BrowserUseApp(integration=integration)
    # app = YahooFinanceApp(integration=None)
    # result=app.get_stock_history("AAPL")


    # app=YoutubeApp(integration=integration)
    # result=app.get_transcript_text("TlibMqj2JUM")
        
        
        
        
    # app=ScraperApp(integration=integration)
    # result = app.linkedin_people_search(keywords="software engineer")
    # result = app.get_stock_info("AAPL")
    # Basic usage - last month of daily data
    # result = app.get_stock_history("AAPL")
    
    # Different periods
    # result = app.get_stock_history("AAPL", period="1y")  # 1 year
    # result = app.get_stock_history("AAPL", period="6mo") # 6 months
    
    # Different intervals
    # result = app.get_stock_history("AAPL", period="5d", interval="1h")  # Hourly data for 5 days
    
    # Specific date range
    # result = app.get_stock_history("AAPL")
    # result = app.get_financial_statements("AAPL")
    # result = app.get_stock_news("AAPL")
    # result = app.get_financial_statements("AAPL", statement_type="cashflow")
    # result = app.get_stock_recommendations("AAPL", rec_type="upgrades_downgrades")
    # result = app.search("Boeing")
    # result = app.lookup_ticker("Apple", lookup_type="stock")
    # result = app.publish_post(
    #     publication_id="68077ed7fe54cfc2a84b253b",
    #     title="My New Post 2",
    #     content="This is my post content in **markdown**",
    #     tags=["tech", "ai", "development"],
    #     cover_image="https://fastly.picsum.photos/id/1053/200/300.jpg?hmac=g-MecQlcjGrVSsQX4Odc3D1ORJuzKsofZ6BIVb1Y4ok"  # Optional
    # )
    # result = await app.browser_task(task="Go to https://www.google.com and search for 'java'")
    result = await app.get_browser_task_status(task_id="942912b9-dbd8-45d8-83a0-8c84f729d95a")
    logger.info(result)
    print(type(result))


if __name__ == "__main__":
    asyncio.run(main())