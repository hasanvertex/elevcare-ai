import streamlit as st
import pandas as pd


def chatbot(manager):

    st.divider()

    st.subheader("🤖 ElevCare AI Agent")

    question = st.text_input(
        "Ask ElevCare AI"
    )

    if st.button("Ask AI"):

        result = manager.ask(question)

        # LIST RESULT
        if isinstance(result, list):

            if len(result) > 0:

                st.dataframe(
                    pd.DataFrame(result),
                    use_container_width=True
                )

            else:

                st.warning(
                    "No records found."
                )

        # DICTIONARY RESULT
        elif isinstance(result, dict):

            if "total" in result:

                col1, col2, col3, col4 = st.columns(4)

                col1.metric(
                    "📄 Total",
                    result["total"]
                )

                col2.metric(
                    "✅ Active",
                    result["active"]
                )

                col3.metric(
                    "❌ Expired",
                    result["expired"]
                )

                col4.metric(
                    "⚠️ Expiring",
                    result["expiring"]
                )

            elif "total_contracts" in result:

                st.metric(
                    "📄 Total Contracts",
                    result["total_contracts"]
                )

            else:

                st.json(result)

        # TEXT RESULT
        else:

            st.info(result)