import streamlit as st
import pandas as pd
import io
from typing import List, Dict

def calculate_seats(df: pd.DataFrame, formula_type: str, total_seats: int) -> pd.DataFrame:
    """
    Calculate seat allocation using D'Hondt or St. Lague method
    
    Args:
        df (pd.DataFrame): DataFrame with party and vote information
        formula_type (str): 'DH' for D'Hondt or 'SL' for St. Lague
        total_seats (int): Total number of seats to allocate
    
    Returns:
        pd.DataFrame: Updated DataFrame with seat allocations
    """
    # Set formula multiplier
    formula_multiplier = 1 if formula_type == 'DH' else 2
    
    # Create a copy of the dataframe to work with
    results_df = df.copy()
    
    # Initialize columns
    results_df['Seats'] = [0] * len(results_df)
    results_df['Quota'] = [0.0] * len(results_df)
    
    # Convert votes to float
    results_df['Votes'] = results_df['Votes'].apply(float)
    
    # Track initial votes
    initial_votes = results_df['Votes'].copy()
    
    # Seat allocation loop
    for _ in range(total_seats):
        # Calculate quota for each party
        for idx in results_df.index:
            results_df.at[idx, 'Quota'] = float(initial_votes[idx]) / (formula_multiplier * float(results_df.at[idx, 'Seats']) + 1)
        
        # Find party with highest quota
        max_quota_idx = results_df['Quota'].idxmax()
        
        # Allocate a seat to that party
        results_df.at[max_quota_idx, 'Seats'] += 1
    
    # Convert seats to integers
    results_df['Seats'] = results_df['Seats'].apply(int)
    
    return results_df

def main():
    st.set_page_config(
        page_title="MMP Seat Calculator",
        page_icon="🗳️",
        layout="wide"
    )
    
    st.title('MMP Seat Allocation Calculator')
    
    # Sidebar for configuration
    st.sidebar.header('Calculator Settings')
    
    # Formula selection
    formula = st.sidebar.selectbox(
        'Select Allocation Formula', 
        ['D\'Hondt (DH)', 'St. Lague (SL)'], 
        index=0
    )
    formula_code = 'DH' if formula == 'D\'Hondt (DH)' else 'SL'
    
    # Total seats input
    total_seats = st.sidebar.number_input(
        'Total Number of Seats', 
        min_value=1, 
        max_value=1000, 
        value=10,
        step=1
    )
    
    # Data input methods
    input_method = st.sidebar.radio(
        'Data Input Method',
        ['Manual Entry', 'Upload Excel/CSV']
    )
    
    df = None
    
    # Data input section
    if input_method == 'Manual Entry':
        # Number of parties input
        num_parties = st.sidebar.number_input(
            'Number of Parties', 
            min_value=2, 
            max_value=20, 
            value=5,
            step=1
        )
        
        # Create input dataframe
        input_data: List[Dict] = []
        
        # Create columns for party inputs
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Party Names")
        with col2:
            st.subheader("Vote Counts")
            
        for i in range(num_parties):
            with col1:
                party = st.text_input(f'Party {i+1}', key=f'party_{i}')
            with col2:
                votes = st.number_input(
                    f'Votes {i+1}', 
                    min_value=0, 
                    value=0, 
                    step=1,
                    key=f'votes_{i}'
                )
            
            if party and votes > 0:
                input_data.append({'Party': party, 'Votes': votes})
        
        if input_data:
            df = pd.DataFrame(input_data)
    
    else:
        # File upload
        st.info("Upload a file with two columns: 'Party' and 'Votes'")
        uploaded_file = st.file_uploader(
            'Upload Excel or CSV file', 
            type=['xlsx', 'csv']
        )
        
        if uploaded_file is not None:
            try:
                if uploaded_file.name.endswith('.csv'):
                    df = pd.read_csv(uploaded_file)
                else:
                    df = pd.read_excel(uploaded_file)
                
                # Ensure correct column names
                if len(df.columns) != 2:
                    st.error("File must have exactly two columns: 'Party' and 'Votes'")
                    return
                    
                df.columns = ['Party', 'Votes']
                
            except Exception as e:
                st.error(f"Error reading file: {e}")
                return
        else:
            st.warning('Please upload a file')
            return
    
    # Validate input
    if df is None or df.empty:
        st.warning('Please enter party and vote data')
        return
    
    # Check for valid votes
    if (df['Votes'] <= 0).any():
        st.error('All vote counts must be positive numbers')
        return
    
    # Perform seat allocation
    try:
        results_df = calculate_seats(df, formula_code, total_seats)
        
        # Display results
        st.header('Seat Allocation Results')
        
        # Format results for display
        display_df = results_df.copy()
        display_df['Votes'] = display_df['Votes'].apply(lambda x: f"{int(x):,}")
        display_df['Quota'] = display_df['Quota'].apply(lambda x: f"{x:.2f}")
        
        # Calculate percentages
        total_votes = results_df['Votes'].sum()
        total_seats = results_df['Seats'].sum()
        
        display_df['Vote %'] = results_df['Votes'].apply(lambda x: f"{(x/total_votes)*100:.1f}%")
        display_df['Seat %'] = results_df['Seats'].apply(lambda x: f"{(x/total_seats)*100:.1f}%")
        
        # Reorder columns
        display_df = display_df[['Party', 'Votes', 'Vote %', 'Seats', 'Seat %', 'Quota']]
        
        st.dataframe(display_df, use_container_width=True)
        
        # Visualization
        st.header('Seat Distribution')
        chart_df = pd.DataFrame({
            'Party': results_df['Party'],
            'Seats': results_df['Seats'],
            'Votes %': results_df['Votes'].apply(lambda x: (x/total_votes)*100)
        })
        
        st.bar_chart(chart_df.set_index('Party')[['Seats']])
        
        # Export options
        st.sidebar.header('Export Results')
        export_format = st.sidebar.selectbox(
            'Export Format', 
            ['CSV', 'Excel']
        )
        
        if st.sidebar.button('Export Results'):
            if export_format == 'CSV':
                csv = display_df.to_csv(index=False)
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name='mmp_seat_allocation.csv',
                    mime='text/csv'
                )
            else:
                buffer = io.BytesIO()
                with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                    display_df.to_excel(writer, index=False)
                buffer.seek(0)
                
                st.download_button(
                    label="Download Excel",
                    data=buffer,
                    file_name='mmp_seat_allocation.xlsx',
                    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
    
    except Exception as e:
        st.error(f"Error calculating seats: {e}")
        raise e

if __name__ == '__main__':
    main()
