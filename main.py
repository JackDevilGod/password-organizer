import streamlit as st

from backend.generator.password_generator import Password_generator


def main():
    st.title("password generator and organiser.")
    st.divider()

    while "password generator" not in st.session_state:
        st.session_state["password generator"] = Password_generator()

    while "character types" not in st.session_state or "selected types" not in st.session_state:
        st.session_state["character types"] = st.session_state["password generator"
                                                               ].get_character_types()
        st.session_state["selected types"] = list(st.session_state["password generator"
                                                                   ].get_selected_characters_types()
                                                  )

    columns = st.columns(len(st.session_state["character types"]))

    for index, column in enumerate(columns):
        with column:
            st.session_state["selected types"][index] = st.checkbox(
                label=st.session_state["character types"][index],
                value=st.session_state["selected types"][index])

    character = st.text_input("input character")

    if character != "":
        left, right = st.columns(2)

        with left:
            if st.button("add to black list"):
                try:
                    st.session_state["password generator"].add_to_blacklist(character)
                except ValueError:
                    st.text("It has to be one character.")

        with right:
            if st.button('Remove from black list'):
                st.session_state["password generator"].delete_from_blacklist(character)

    st.text(f"{st.session_state['password generator'].get_blacklist()}")

    if not any(st.session_state["selected types"]):
        st.text("Please select one set of characters.")
        return

    if (st.session_state["selected types"] !=
            st.session_state["password generator"].get_selected_characters_types()):
        st.session_state["password generator"].set_selected_characters_types(
            tuple(st.session_state["selected types"])
        )

    amount_password = st.slider(
        "amount of passwords",
        min_value=1,
        max_value=50,
        value=3
    )
    password_length = st.number_input(
        "password length",
        min_value=1,
        value=20)

    for _ in range(amount_password):
        st.code(st.session_state["password generator"].generate_password(password_length),
                language=None)


if __name__ == '__main__':
    main()
