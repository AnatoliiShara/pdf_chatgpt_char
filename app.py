
import streamlit as st

def main():
    st.set_page_config(page_title="Chat with multifile PDFs", page_icon=":books:")

    st.header("Chat with multifile PDFs  :books:")
    st.text_input("Ask a question about your documents: ")

    with st.sidebar:
        st.subheader("Your documents")

        # Allow users to upload multiple files
        uploaded_files = st.file_uploader("Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
        st.button("Process")

        # Display the list of uploaded files
        if uploaded_files:
            st.subheader("Uploaded Files:")
            for file in uploaded_files:
                st.write(file.name)

if __name__ == "__main__":
    main()
