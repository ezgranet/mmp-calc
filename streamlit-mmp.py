import streamlit as st
import pandas as pd
import numpy as np
import openpyxl

def calculate_seats(df, formula_type, total_seats):
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
    
    # Initialize seat columns
    results_df['Seats'] = 0
    
    # Track initial votes
    initial_votes = results_df['Votes'].copy()
    
    # Seat allocation loop
    for _ in range(total_seats):
        # Calculate quota for each party
        results_df['Quota'] = initial_votes / (formula_multiplier * results_df['Seats'] + 1)
        
        # Find party with highest quota
        max_quota_index = results_df['Quota'].idxmax()
        
        # Allocate a seat to that party
        results_df.loc[max_quota_index, 'Seats'] += 1
    
    return results_df

def main():
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
        value=10
    )
    
    # Data input methods
    input_method = st.sidebar.radio(
        'Data Input Method',
        ['Manual Entry', 'Upload Excel/CSV']
    )
    
    # Data input section
    if input_method == 'Manual Entry':
        # Number of parties input
        num_parties = st.sidebar.number_input(
            'Number of Parties', 
            min_value=2, 
            max_value=20, 
            value=5
        )
        
        # Create input dataframe
        input_data = []
        for i in range(num_parties):
            cols = st.columns(2)
            with cols[0]:
                party = st.text_input(f'Party {i+1} Name', key=f'party_{i}')
            with cols[1]:
                votes = st.number_input(f'Party {i+1} Votes', min_value=0, key=f'votes_{i}')
            
            if party and votes:
                input_data.append({'Party': party, 'Votes': votes})
        
        df = pd.DataFrame(input_data)
    
    else:
        # File upload
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
    
    # Perform seat allocation
    results_df = calculate_seats(df, formula_code, total_seats)
    
    # Display results
    st.header('Seat Allocation Results')
    st.dataframe(results_df)
    
    # Visualization
    st.header('Seat Distribution')
    st.bar_chart(results_df.set_index('Party')['Seats'])
    
    # Export options
    st.sidebar.header('Export Results')
    export_format = st.sidebar.selectbox(
        'Export Format', 
        ['CSV', 'Excel']
    )
    
    if st.sidebar.button('Export Results'):
        if export_format == 'CSV':
            csv = results_df.to_csv(index=False)
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name='mmp_seat_allocation.csv',
                mime='text/csv'
            )
        else:
            excel_buffer = results_df.to_excel(index=False)
            st.download_button(
                label="Download Excel",
                data=excel_buffer,
                file_name='mmp_seat_allocation.xlsx',
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )

if __name__ == '__main__':
    main()
