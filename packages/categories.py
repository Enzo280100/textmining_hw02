import pandas as pd

def create_broad_categories(category):
    """
    This function maps a given category to one of the broad categories: 
    'Geography & Places', 'Technology & Digital Economy', 'Lifestyle & Wellness', 
    'Arts, Culture & Entertainment', 'Knowledge & Current Affairs'. If not mapped, returns 'Uncategorized'.
    """
    # Geography & Places
    geography_places = {
        'Nepal', 'New Zealand', 'Europe', 'Oman', 'Pakistan', 'Papua New Guinea', 'Poland',
        'Panama', 'Peru', 'America', 'Philippines', 'Palau', 'Armenia', 'Puerto Rico',
        'Qatar', 'Singapore', 'Uganda', 'Africa', 'Russian Federation', 'Portugal',
        'Paraguay', 'Romania', 'Ghana', 'Congo, The Democratic Republic of',
        'Kazakhstan', 'Palestine, State of', 'Rwanda', 'Saudi Arabia', 'Sudan', 'Senegal',
        'Somalia', 'Sierra Leone', 'El Salvador', 'Serbia', 'San Marino', 'Tonga',
        'South Sudan', 'Suriname', 'Slovakia', 'Ukraine', 'Slovenia', 'Sweden',
        'Seychelles', 'Tunisia', 'Turkey', 'Taiwan, Province of China', 'United States',
        'Uruguay', 'Uzbekistan', 'Virgin Islands, U.S.', 'Viet Nam', 'Vanuatu', 'Samoa',
        'Yemen', 'South Africa', 'Zambia', 'Zimbabwe', 'Chad', 'Thailand', 'Tajikistan',
        'Turkmenistan', 'Bulgaria', 'Austria', 'Australia', 'Bangladesh', 'Djibouti',
        'Italy', 'Kyrgyzstan', 'Israel', 'Lithuania', 'Afghanistan', 'Aruba', 'Angola',
        'Albania', 'United Arab Emirates', 'Andorra', 'Guernsey', 'Argentina', 'Antarctica',
        'Guam', 'Azerbaijan', 'Haiti', 'Burundi', 'Belgium', 'Benin', 'Burkina Faso',
        'Latvia', 'Bahrain', 'Bahamas', 'Bosnia and Herzegovina', 'Belarus', 'Belize',
        'Brazil', 'Bermuda', 'Barbados', 'Bhutan', 'Botswana', 'Central African Republic',
        'Canada', 'Switzerland', 'Chile', 'China', "Côte d'Ivoire", 'Cameroon', 'Congo',
        'Colombia', 'Germany', 'Cyprus', 'Cabo Verde', 'Costa Rica', 'Cuba',
        'Christmas Island', 'Cayman Islands', 'Denmark', 'Dominican Republic', 'Algeria',
        'Eritrea', 'Ecuador', 'Egypt', 'Estonia', 'Georgia', 'Iceland', 'Spain',
        'Ethiopia', 'Gabon', 'Finland', 'Fiji', 'France', 'United Kingdom', 'Gibraltar',
        'Guinea', 'Greece', 'Gambia', 'Iran, Islamic Republic of', 'Greenland', 'Ireland',
        'India', 'Guatemala', 'Guyana', 'Hong Kong', 'Iraq', 'Croatia', 'Honduras',
        'Hungary', 'Indonesia', 'Isle of Man', 'Jamaica', 'Kenya', 'Jersey', 'Malawi',
        'Jordan', 'Japan', 'Nigeria', 'Cambodia', 'Korea, Republic of', 'Lebanon',
        'Kuwait', 'Libya', 'Liberia', 'Liechtenstein', 'Sri Lanka', 'Luxembourg', 'Macao',
        'Morocco', 'Monaco', 'Maldives', 'Mexico', 'Mali', 'Malaysia', 'Netherlands',
        'Norway', 'Myanmar', 'Madagascar', 'North Macedonia', 'Malta', 'Mongolia',
        'Montenegro', 'Montserrat', 'Mozambique', 'Mauritania', 'Mauritius', 'Martinique',
        'Niger', 'Nicaragua', 'Namibia', 'Réunion', 'Asia', 'world', 'Travel', 'Hiking'
    }

    # Technology & Digital Economy
    tech_business = {
        'Technology', 'Artificial Intelligence', 'Coding', 'Virtual Reality', 'Google',
        'YouTube', 'Facebook', 'Amazon', 'COVID', 'Instagram', 'TikTok', 'Blockchain',
        'Cryptocurrency', 'Bitcoin', 'Real estate', 'Stock', 'Finance', 'Jobs',
        'Startups', 'Entrepreneurship', 'Productivity', 'Cars'
    }

    # Lifestyle & Wellness
    lifestyle_wellness = {
        'Health', 'Fitness', 'Yoga', 'Meditation', 'Mindfulness', 'Nutrition', 'Vegan',
        'Beauty', 'Fashion', 'Sports', 'Recipes', 'Food', 'DIY', 'Gardening', 'Pets',
        'Home', 'Happiness', 'Minimalism'
    }

    # Arts, Culture & Entertainment
    arts_culture = {
        'Art', 'Music', 'Movies', 'Photography', 'Design', 'Architecture', 'Poetry',
        'Anime', 'Games', 'Podcasts', 'Love', 'Relationships'
    }

    # Knowledge & Current Affairs
    knowledge_affairs = {
        'Education', 'Science', 'History', 'Psychology', 'Space', 'News', 'Politics',
        'Climate', 'Sustainability', 'Weather', 'Philosophy', 'Astronomy', 'Parenting',
        'Motivation'
    }

    # Create the mapping dictionary
    category_mapping = {
        'Geography & Places': geography_places,
        'Technology & Digital Economy': tech_business,
        'Lifestyle & Wellness': lifestyle_wellness,
        'Arts, Culture & Entertainment': arts_culture,
        'Knowledge & Current Affairs': knowledge_affairs
    }
    
    # Find the broad category
    for broad_cat, items in category_mapping.items():
        if category in items:
            return broad_cat
    
    return 'Uncategorized'


def categorize_articles(df):
    """
    This function adds a new column 'Broad_category' to the DataFrame df based on the category column.
    It also drops any rows that are labeled 'Uncategorized'.
    """
    # Apply the broad category function
    df['Broad_category'] = df['category'].apply(create_broad_categories)

    # Check for uncategorized rows
    unrecognized = df[df['Broad_category'] == 'Uncategorized']['category'].unique()
    if len(unrecognized) > 0:
        print("Uncategorized categories:", unrecognized)

    # Drop rows with 'Uncategorized' categories
    df.drop(df[df['Broad_category'] == 'Uncategorized'].index, inplace=True)

    return df


