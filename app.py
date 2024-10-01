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

# Tab 2: Task Steps with calculated sums displayed
with tab2:
    st.subheader("Task Steps")

    # Step 1 Tasks
    step1_sum = 0
    step1_sum += st.number_input("1.1. Create Summary page", min_value=0, value=0)
    step1_sum += st.number_input("1.2. Deduplicate data", min_value=0, value=0)
    step1_sum += st.number_input("1.3. Data Category filtering", min_value=0, value=0)
    step1_sum += st.number_input("1.4. Cross-referencing: Fuzzy matching with AP", min_value=0, value=0)
    step1_sum += st.number_input("1.5. Create Existing merchants and New merchants tables", min_value=0, value=0)
    step1_sum += st.number_input("1.6. Review Fuzzy Matches", min_value=0, value=0)
    step1_sum += st.number_input("1.7. Add non-approved fuzzy matches to New Merchants", min_value=0, value=0)
    step1_sum += st.number_input("1.8. Create new tabs/sheets for each segment", min_value=0, value=0)
    step1_sum += st.number_input("1.9. Split existing merchants into reviewed and not reviewed", min_value=0, value=0)
    step1_sum += st.number_input("1.10. Check Existing merchant's last 'Reviewed At' date", min_value=0, value=0)

    st.write(f"1. Data Reception & Filtering (Total: {step1_sum})")
    with st.expander("1. Data Reception & Filtering"):
        st.write(f"Total for Step 1: {step1_sum}")

    # Step 2 Tasks
    step2_sum = 0
    step2_sum += st.number_input("2.1. Profile Creation for New Merchants - Week 1", min_value=0, value=0)
    step2_sum += st.number_input("2.2. Raise queries with Visa about merchants", min_value=0, value=0)
    step2_sum += st.number_input("2.3. Profile Creation for New Merchants - Week 2", min_value=0, value=0)
    step2_sum += st.number_input("2.4. New Merchants Confirm Entity", min_value=0, value=0)
    step2_sum += st.number_input("2.5. New Merchants Prioritisation", min_value=0, value=0)
    step2_sum += st.number_input("2.6. New Merchants Scraping", min_value=0, value=0)
    step2_sum += st.number_input("2.7. New Merchants Order", min_value=0, value=0)
    step2_sum += st.number_input("2.8. New Merchants Documentation", min_value=0, value=0)
    step2_sum += st.number_input("2.9. Existing Merchants Category Matching", min_value=0, value=0)
    step2_sum += st.number_input("2.10. Existing Merchants Prioritisation", min_value=0, value=0)
    step2_sum += st.number_input("2.11. Existing Merchants Profile Review", min_value=0, value=0)
    step2_sum += st.number_input("2.12. Existing Merchants Scraping", min_value=0, value=0)
    step2_sum += st.number_input("2.13. Existing Merchants Documentation", min_value=0, value=0)

    st.write(f"2. Data Coverage (Total: {step2_sum})")
    with st.expander("2. Data Coverage"):
        st.write(f"Total for Step 2: {step2_sum}")

    # Step 3 Tasks
    step3_sum = st.number_input("3. Coverage Estimate/Checkpoint Analysis", min_value=0, value=0)

    st.write(f"3. CHECK POINT – Coverage Estimate (Total: {step3_sum})")
    with st.expander("3. CHECK POINT – Coverage Estimate"):
        st.write(f"Total for Step 3: {step3_sum}")

    # Step 4 Tasks
    step4_sum = 0
    step4_sum += st.number_input("4.1.1. Ratings: (A) New merchants analysis (size S)", min_value=0, value=0)
    step4_sum += st.number_input("4.1.2. Ratings: (B) Existing merchants analysis (size S)", min_value=0, value=0)
    step4_sum += st.number_input("4.1.3. Ratings: (B) 2nd Priority analysis (size S)", min_value=0, value=0)
    step4_sum += st.number_input("4.2.1. Ratings: (A) New merchants analysis (size M & L)", min_value=0, value=0)
    step4_sum += st.number_input("4.2.2. Ratings: (B) Existing merchants analysis (size M & L)", min_value=0, value=0)
    step4_sum += st.number_input("4.2.3. Ratings: (B) 2nd Priority analysis (size M & L)", min_value=0, value=0)
    step4_sum += st.number_input("4.2.3. Ratings: (B) 2nd Priority analysis (size M & L)", min_value=0, value=0)

    st.write(f"4. Ratings (Total: {step4_sum})")
    with st.expander("4. Ratings"):
        st.write(f"Total for Step 4: {step4_sum}")

    # Step 5 Tasks
    step5_sum = 0
    step5_sum += st.number_input("5.1. Final Review", min_value=0, value=0)
    step5_sum += st.number_input("5.2. Performance Metrics", min_value=0, value=0)
    step5_sum += st.number_input("5.3. Feedback Collection", min_value=0, value=0)
    step5_sum += st.number_input("5.4. Process Optimization", min_value=0, value=0)
    step5_sum += st.number_input("5.5. Implementation of Improvements", min_value=0, value=0)
    step5_sum += st.number_input("5.6. Documentation Update", min_value=0, value=0)
    step5_sum += st.number_input("5.7. Client Reporting", min_value=0, value=0)
    step5_sum += st.number_input("5.8. Continuous Monitoring", min_value=0, value=0)

    st.write(f"5. Final Review & Metrics (Total: {step5_sum})")
    with st.expander("5. Final Review & Metrics"):
        st.write(f"Total for Step 5: {step5_sum}")

    # Grand total of all steps
    total_sum = step1_sum + step2_sum + step3_sum + step4_sum + step5_sum
    st.subheader(f"Grand Total for all steps: {total_sum}")
