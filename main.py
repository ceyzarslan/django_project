import streamlit as st
from config import engine, get_session
from models import Base

# Veritabanı tablolarını oluşturur
Base.metadata.create_all(bind=engine)


def main():
    # Oturum oluştur
    Session = get_session()

    st.title("Product Management Dashboard")
    st.divider()

    # Sidebar'da seçim yapma bölümü
    option = st.sidebar.selectbox("Dashboard", ("Products", "Brand", "Categories"))

    # Kullanıcının seçimine göre içerik göster
    if option == "Products":
        st.subheader("Product Management")
        # Ürün yönetimi için kod buraya gelecek

    elif option == "Brand":
        st.subheader("Brand Management")
        # Marka yönetimi için kod buraya gelecek

    elif option == "Categories":
        st.subheader("Category Management")
        # Kategori yönetimi için kod buraya gelecek


# Ana fonksiyonu çalıştır
if __name__ == '__main__':
    main()
