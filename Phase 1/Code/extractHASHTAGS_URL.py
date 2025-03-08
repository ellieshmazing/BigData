import json

def extract_unique_hashtags_and_urls(file_path):
    """
    Hashtags and URLs
    """
    all_hashtags = []
    all_urls = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if not line.strip():
                    continue
                try:
                    tweet = json.loads(line.strip())
                    if 'entities' in tweet:
                        # hashtags
                        if 'hashtags' in tweet['entities']:
                            for hashtag in tweet['entities']['hashtags']:
                                if 'text' in hashtag:
                                    all_hashtags.append(hashtag['text'])
                        
                        # URLs
                        if 'urls' in tweet['entities']:
                            for url_obj in tweet['entities']['urls']:
                                if 'expanded_url' in url_obj:
                                    all_urls.append(url_obj['expanded_url'])
                        
                        # media URLs
                        if 'media' in tweet['entities']:
                            for media in tweet['entities']['media']:
                                if 'expanded_url' in media:
                                    all_urls.append(media['expanded_url'])
                    
                    # extended entities
                    if 'extended_entities' in tweet and 'media' in tweet['extended_entities']:
                        for media in tweet['extended_entities']['media']:
                            if 'expanded_url' in media:
                                all_urls.append(media['expanded_url'])
                    
                    # retweets might have these
                    if 'retweeted_status' in tweet and 'entities' in tweet['retweeted_status']:
                        rt_entities = tweet['retweeted_status']['entities']
                        
                        # hashtags
                        if 'hashtags' in rt_entities:
                            for hashtag in rt_entities['hashtags']:
                                if 'text' in hashtag:
                                    all_hashtags.append(hashtag['text'])
                        
                        # URLs
                        if 'urls' in rt_entities:
                            for url_obj in rt_entities['urls']:
                                if 'expanded_url' in url_obj:
                                    all_urls.append(url_obj['expanded_url'])
                                    
                except json.JSONDecodeError:
                    print(f"JSON ERROR")
                except Exception as e:
                    print(f"Error processing tweet: {str(e)}")
        
        # cut duplicates
        unique_hashtags = sorted(set(all_hashtags))
        unique_urls = sorted(set(all_urls))
        
        return unique_hashtags, unique_urls
        
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return [], []
    
def extract_hashtags_and_urls(file_path):
    """
    Hashtags and URLs
    """
    all_hashtags = []
    all_urls = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if not line.strip():
                    continue
                try:
                    tweet = json.loads(line.strip())
                    if 'entities' in tweet:
                        # hashtags
                        if 'hashtags' in tweet['entities']:
                            for hashtag in tweet['entities']['hashtags']:
                                if 'text' in hashtag:
                                    all_hashtags.append(hashtag['text'])
                        
                        # URLs
                        if 'urls' in tweet['entities']:
                            for url_obj in tweet['entities']['urls']:
                                if 'expanded_url' in url_obj:
                                    all_urls.append(url_obj['expanded_url'])
                        
                        # media URLs
                        if 'media' in tweet['entities']:
                            for media in tweet['entities']['media']:
                                if 'expanded_url' in media:
                                    all_urls.append(media['expanded_url'])
                    
                    # extended entities
                    if 'extended_entities' in tweet and 'media' in tweet['extended_entities']:
                        for media in tweet['extended_entities']['media']:
                            if 'expanded_url' in media:
                                all_urls.append(media['expanded_url'])
                    
                    # retweets might have these
                    if 'retweeted_status' in tweet and 'entities' in tweet['retweeted_status']:
                        rt_entities = tweet['retweeted_status']['entities']
                        
                        # hashtags
                        if 'hashtags' in rt_entities:
                            for hashtag in rt_entities['hashtags']:
                                if 'text' in hashtag:
                                    all_hashtags.append(hashtag['text'])
                        
                        # URLs
                        if 'urls' in rt_entities:
                            for url_obj in rt_entities['urls']:
                                if 'expanded_url' in url_obj:
                                    all_urls.append(url_obj['expanded_url'])
                                    
                except json.JSONDecodeError:
                    print(f"JSON ERROR")
                except Exception as e:
                    print(f"Error processing tweet: {str(e)}")
        
        return all_hashtags, all_urls
        
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return [], []

'''ORIGINAL CODE WITH UNIQUE HASHTAGS/URLS AND SUMMARY INFO
def main():
    file_path = 'out.json'
    output_file = 'output.txt'
    
    hashtags, urls = extract_unique_hashtags_and_urls(file_path)
    
    # Write results to output.txt
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("Hashtags found:\n")
        for hashtag in hashtags:
            f.write(f"#{hashtag}\n")
        
        f.write("\nURLs found:\n")
        for url in urls:
            f.write(f"{url}\n")
        
        f.write(f"\nSummary: Found {len(hashtags)} unique hashtags and {len(urls)} unique URLs\n")
    
    print(f"Results written to {output_file}")'''
    
def main():
    file_path = '../Tweets/out.json'
    output_file_hashtags = '../Output/outputHashtags.txt'
    output_file_urls = '../Output/outputURLs.txt'
    
    hashtags, urls = extract_hashtags_and_urls(file_path)
    
    # Write hashtags to outputHashtags.txt
    with open(output_file_hashtags, 'w', encoding='utf-8') as f:
        for hashtag in hashtags:
            f.write(f"#{hashtag}\n")
            
    print(f"Hashtags written to {output_file_hashtags}")
            
    # Write URLs to outputURLs.txt
    with open(output_file_urls, 'w', encoding='utf-8') as f:
        for url in urls:
            f.write(f"{url}\n")
        
    
    print(f"URLs written to {output_file_urls}")

if __name__ == "__main__":
    main()
