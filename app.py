import streamlit as st

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

# Tab 2: Task Steps - Manually create the toggle list for tasks
with tab2:
    st.subheader("Task Steps")

    # Step 1 Tasks
    with st.expander("Data Reception & Filtering"):
        st.write("1.1. Create Summary page")
        st.write("1.2. Deduplicate data")
        st.write("1.3. Data Category filtering - Filter the merchants by categories.")
        st.write("1.4. Cross-referencing: Fuzzy matching with AP - we didn't do AKA")
        st.write("1.5. Create Existing merchants and New merchants tables")
        st.write("1.6. Review Fuzzy Matches - Review the fuzzy match results to make sure they're actually matches")
        st.write("1.7. Add non-approved fuzzy matches to New Merchants")
        st.write("1.8. Create new tabs/sheets for each segment")
        st.write("1.9. Split existing merchants into reviewed and not reviewed")
        st.write("1.10. Check Existing (reviewed) merchant's last 'Reviewed At' date")

    # Step 2 Tasks
    with st.expander("Data Coverage"):
        st.write("2.1. Profile Creation for New Merchants - Week 1 (starting 11/09/2024)")
        st.write("2.2. Raise queries with Visa about merchants")
        st.write("2.3. Profile Creation for New Merchants - Week 2")
        st.write("2.4. New Merchants Confirm Entity - Check websites and names of created profiles and ensure no duplicates")
        st.write("2.5. New Merchants Prioritisation - Organise merchants by category and size, prioritising the largest first")
        st.write("2.6. New Merchants Scraping - Team 1 runs the scraper on all new profiles in order of priority")
        st.write("2.7. New Merchants Order - Rearrange the merchant list by total number of PPs found")
        st.write("2.8. New Merchants Documentation - Create a summary table for (A) New merchants")
        st.write("2.9. Existing Merchants Category Matching")
        st.write("2.10. Existing Merchants Prioritisation")
        st.write("2.11. Existing Merchants Profile Review")
        st.write("2.12. Existing Merchants Scraping")
        st.write("2.13. Existing Merchants Documentation")

    # Step 3 Tasks
    with st.expander("CHECK POINT – Coverage Estimate "):
        st.write("3. Coverage Estimate/Checkpoint Analysis - Analyse the number of companies we have in each category and size")

    # Step 4 Tasks
    with st.expander("Ratings"):
        st.write("4.1.1. Ratings: (A) New merchants analysis (size S)")
        st.write("4.1.2. Ratings: (B) Existing merchants analysis (size S)")
        st.write("4.1.3. Ratings: (B) 2nd Priority analysis (size S)")
        st.write("4.2.1. Ratings: (A) New merchants analysis (size M & L)")
        st.write("4.2.2. Ratings: (B) Existing merchants analysis (size M & L)")
        st.write("4.2.3. Ratings: (B) 2nd Priority analysis (size M & L)")

    # Step 5 Tasks
    with st.expander("Process Conclusion and Continuous Improvement"):
        st.write("5.1. Final Review")
        st.write("5.2. Performance Metrics")
        st.write("5.3. Feedback Collection")
        st.write("5.4. Process Optimization")
        st.write("5.5. Implementation of Improvements")
        st.write("5.6. Documentation Update")
        st.write("5.7. Client Reporting")
        st.write("5.8. Continuous Monitoring")
