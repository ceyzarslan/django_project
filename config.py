from sqlalchemy import create_engine  # SQLAlchemy'den create_engine fonksiyonunu import ediyoruz. Bu fonksiyon, veritabanına bağlantı kurmak için kullanılıyor.
from sqlalchemy.orm import sessionmaker  # SQLAlchemy'den sessionmaker'ı import ediyoruz. Bu, veritabanı işlemlerinde oturum (session) yaratmak için kullanılıyor.

CONNECTION_STRING = "sqlite:///data.db"  # Veritabanı bağlantısı için bir bağlantı dizesi tanımlıyoruz. Burada SQLite veritabanını kullanıyoruz ve "data.db" dosyası oluşturulacak.

engine = create_engine(CONNECTION_STRING)  # create_engine fonksiyonunu kullanarak veritabanı motorunu (engine) oluşturuyoruz ve bağlantı kuruyoruz.

Session = sessionmaker(bind=engine)  # sessionmaker ile oturum fonksiyonunu oluşturuyoruz ve bu oturum, veritabanı motoruna bağlanacak şekilde ayarlanıyor.

def get_session():  # Veritabanı ile etkileşim kurmak için oturum döndüren bir fonksiyon tanımlıyoruz.
    return Session()  # Bu fonksiyon çağrıldığında yeni bir oturum (session) döndürüyoruz.



