import recordlinkage
import pandas as pd

from afi_scraping import scrape_afi
from criterion_scraping import scrape_criterion
from bfi_scraping import scrape_bfi
from loc_scraping import scrape_loc
from tspdt_scraping import scrape_tspdt


# Our goal is given 5 lists of movies to create a single list containing all the movies from the 5 lists,
# without any duplicates.
# We will use recordlinkage to match the movies from the 5 lists. We use recordlinkage istead of a simple concat
# because the titles in the 5 lists may not be exactly the same.
def match():

    afi_list = scrape_afi()
    criterion_list = scrape_criterion()
    bfi_list = scrape_bfi()
    loc_list = scrape_loc()
    tspdt_list = scrape_tspdt()

    dataframes = [afi_list, criterion_list, bfi_list, loc_list, tspdt_list]
    duplicates_df = pd.DataFrame(columns=['title', 'year'])

    indexer = recordlinkage.Index()
    indexer.full()

    # Recordlinkage can only handle two dataframes at a time, so we need to compare each dataframe with the others
    # iteratively
    for i in range(len(dataframes) - 1):
        for j in range(i + 1, len(dataframes)):
            df1 = dataframes[i]
            df2 = dataframes[j]

            pairs = indexer.index(df1, df2)
            compare = recordlinkage.Compare()

            compare.string('title', 'title', method='jarowinkler', threshold=0.85, label='title')

            # Compare 'year' column only when it is not null
            compare.exact('year', 'year', label='year')

            features = compare.compute(pairs, df1, df2)

            # Using recordlinkage we find all potential duplicates
            potential_duplicates = features[features.sum(axis=1) >= 1]

            # We add the potential duplicates to the duplicates_df dataframe
            for idx in potential_duplicates.index:
                title = df1.loc[idx[0], 'title']
                year = df1.loc[idx[0], 'year']
                duplicates_df.loc[len(duplicates_df)] = [title, year]

            # Some lists (BFI for example) don't have the year of the movie
            missing_year_idx = df2['year'].isnull()
            for idx in missing_year_idx[missing_year_idx].index:
                title = df2.loc[idx, 'title']
                duplicates_df.loc[idx] = [title, None]

    duplicates_df.drop_duplicates(inplace=True)
    merged_df = pd.concat(dataframes)
    merged_df.drop_duplicates(subset='title', inplace=True)
    merged_df.to_csv('duplicates.csv', index=False)

    return merged_df

