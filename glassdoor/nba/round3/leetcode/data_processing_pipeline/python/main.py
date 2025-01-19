from data_processor import DataProcessor
from web_crawler_data_pipeline import WebCrawlerDataPipeline

def deploy_data_processor():
    # Sample NBA player data
    nba_data = [
        {"name": "LeBron James", "team": "Lakers", "stats": "25.7 PPG, 7.9 RPG, 7.6 APG"},
        {"name": "Kevin Durant", "team": "Suns", "stats": "29.1 PPG, 6.7 RPG, 5.0 APG"},
        {"name": "Giannis Antetokounmpo", "team": "Bucks", "stats": "31.1 PPG, 11.8 RPG, 5.7 APG"},
        {"name": "Stephen Curry", "team": "Warriors", "stats": "29.4 PPG, 6.1 RPG, 6.3 RPG"},
        {"name": "Nikola Jokic", "team": "Nuggets", "stats": "24.5 PPG, 11.8 RPG, 9.8 RPG"},
    ]

    processor = DataProcessor(num_threads=3)
    result = processor.run(nba_data)

    print("Processed NBA Player Data")
    for item in result:
        print(item)

def deploy_nba_web_crawler_pipeline():
    start_url = "https://www.nba.com/players"
    pipeline = WebCrawlerDataPipeline(start_url, num_threads=5)
    print(f"Starting NBA data pipeline from: {start_url}")
    results = pipeline.run()
    print(f"Processing complete. Total players processed: {len(results)}")

    for player in results[:5]:
        print(f"Player: {player['name']}, Stats: {player['stats']}")

def main():
    deploy_data_processor()

    # deploy_nba_web_crawler_pipeline()
    
if __name__ == "__main__":
    main()
