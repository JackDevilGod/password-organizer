import streamlit as st
import pandas as pd

from backend.orginiser.dataframe_functions import preprocess_dataframe


def main():
    st.title("password organiser")
    st.divider()
    if "last" not in st.session_state:
        st.session_state["last"] = None

    uploaded_file = st.file_uploader(("upload csv with tab as separator." +
                                      "With headers of website, password, username"),
                                     type="csv",
                                     accept_multiple_files=False)

    if uploaded_file is not None and st.session_state["last"] != uploaded_file:
        st.session_state["last"] = uploaded_file
        st.session_state["csv"], st.session_state["csv stat"] = preprocess_dataframe(
            pd.read_csv(uploaded_file,
                        sep="\t",
                        header=0,
                        index_col=False))

    if st.button("Create empty dataframe."):
        st.session_state["csv"] = pd.DataFrame([], columns=["Website", "Password", "Username"])
        st.session_state["csv stat"] = [0 for _ in range(3)]
        st.session_state["last"] = None

    if ("csv" not in st.session_state or st.session_state["csv"] is None or
        len(st.session_state["csv"].columns) != 3 or
            not (["Website", "Password", "Username"] == st.session_state["csv"].columns).all()):
        return

    st.divider()

    if "input" not in st.session_state:
        st.session_state["input"] = ["" for _ in range(3)]
        st.session_state["last input"] = None

    input_left, input_center, input_right = st.columns(3)

    with input_left:
        pass

    st.text(f"{st.session_state['csv stat']}")
    st.dataframe(st.session_state["csv"])


if __name__ == '__main__':
    main()
