import streamlit as st

def main():
    st.title("Limbus Company E.G.O Gift Checker")
    
    # File uploader
    uploaded_file = st.file_uploader("Upload a screenshot", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Screenshot", use_column_width=True)
        st.success("File uploaded successfully!")

if __name__ == "__main__":
    main()
