import streamlit as st
import pandas as pd

# Load task data from the CSV file
file_path = '/mnt/data/Time Management (1).csv'
task_data = pd.read_csv(file_path)

# Create tabs for the application
tab1, tab2 = st.tabs(["Merchant Cost Calculator", "Task Steps"])

# Tab 1: Merchant Cost Calculator logic
with tab1:
    st.title("Client Data - Merchant Cost Calculator")

    # Input Fields for OOS Merchants
    oos_merchants = st.number_input('Number of OOS & duplicate merchants', min_value=0, value=0)

    # Size of Merchants
    even_distribution = st.checkbox('Even distribution of large, medium, & small merchants')

    if even_distribution:
        total_non_oos_merchants = st.number_input('Total number of non-OOS merchants', min_value=0, value=0)
        
        # Evenly distribute across large, medium, and small merchants
        large_merchants = total_non_oos_merchants // 3
        medium_merchants = total_non_oos_merchants // 3
        small_merchants = total_non_oos_merchants - (large_merchants + medium_merchants)  # Remaining merchants go to small
    else:
        large_merchants = st.number_input('Number of large merchants', min_value=0, value=0)
        medium_merchants = st.number_input('Number of medium merchants', min_value=0, value=0)
        small_merchants = st.number_input('Number of small merchants', min_value=0, value=0)
        total_non_oos_merchants = large_merchants + medium_merchants + small_merchants

    # Verified vs Unverified selections
    st.subheader('Choose verification for proofpoints and policies')
    proofpoint_type = st.radio("Proofpoints", ('Verified', 'Unverified'))
    policy_type = st.radio("Policies", ('Verified', 'Unverified'))

    # Constants for times (in minutes)
    profile_creation_time = 10
    oos_time = 2
    verified_proofpoints_times = {'large': 60, 'medium': 40, 'small': 15}
    unverified_proofpoints_time = 2
    verified_policies_times = {'large': 480, 'medium': 300, 'small': 180}
    unverified_policies_time = 10

    # Calculation Logic
    def calculate_cost(oos_merchants, large, medium, small, proofpoint_type, policy_type):
        # Time for OOS merchants
        total_time = oos_merchants * oos_time
        
        # Proofpoints and Policies times
        if proofpoint_type == 'Verified':
            proofpoints_times = verified_proofpoints_times
        else:
            proofpoints_times = {'large': unverified_proofpoints_time, 'medium': unverified_proofpoints_time, 'small': unverified_proofpoints_time}
        
        if policy_type == 'Verified':
            policies_times = verified_policies_times
        else:
            policies_times = {'large': unverified_policies_time, 'medium': unverified_policies_time, 'small': unverified_policies_time}

        # Calculate times for large, medium, and small merchants
        for size, count in zip(['large', 'medium', 'small'], [large, medium, small]):
            total_time += count * (profile_creation_time + proofpoints_times[size] + policies_times[size])

        return total_time

    # Calculate total cost
    total_cost = calculate_cost(oos_merchants, large_merchants, medium_merchants, small_merchants, proofpoint_type, policy_type)

    # Display the total time cost
    st.subheader("Total Time Cost")
    st.write(f"Total cost in minutes: {total_cost}")

# Tab 2: Task Steps - Dynamically create the toggle list for tasks from the CSV file
with tab2:
    st.subheader("Task Steps")

    # Get unique major steps (Step column)
    major_steps = task_data['Step'].dropna().unique()

    # Loop through each major step
    for step in major_steps:
        # Create an expander for each major step
        with st.expander(f"{int(step)}. Task Steps Group {int(step)}"):
            # Filter tasks belonging to this major step
            step_tasks = task_data[task_data['Step'] == step]

            # Loop through each sub-task under the current major step
            for _, row in step_tasks.iterrows():
                task = row['Task']
                description = row['Task Description'] if not pd.isna(row['Task Description']) else ''
                st.write(f"{row['Steps']} {task} - {description}")
