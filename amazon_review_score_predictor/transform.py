import pandas as pd
import os

def filter_dataset_by_language(filename, language, index_col=0):
    print(f"Processing {filename}.csv...")
    
    input_path = os.path.join('../data/raw', f'{filename}.csv')
    df = pd.read_csv(input_path, index_col=index_col)
    
    df_filtered = df[df['language'] == language]

    os.makedirs('../data/processed', exist_ok=True)

    output_path = os.path.join('../data/processed', f'{filename}.csv')
    df_filtered.to_csv(output_path, index=False)

    original_records = len(df)
    filtered_records = len(df_filtered)

    return {
        'filename': filename,
        'original_records': original_records,
        'filtered_records': filtered_records,
        'percentage': round(100 * filtered_records / original_records, 2) if original_records > 0 else 0,
        'unique_languages': df_filtered['language'].unique().tolist()
    }
