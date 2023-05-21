import streamlit as st


def main():
    #---- mengatur lebar tampilan -----
    st.markdown('<style>body{max-width: 800px; margin: auto;}</style>', unsafe_allow_html=True)

    # Import Foto
    profile_pic = './images/foto_cv.jpeg'
    st.image(profile_pic,width=150,caption='Foto Profil', output_format='JPEG') #menampilkan foto

    # --- Title ----
    st.title('Resume 🀄')

    # Informasi pribadi
    st.header('About Me 😉')
    st.markdown('''
                Bayuzen adalah Seorang :red[Data Scientist]: yang sudah berpengalaman kurang lebih 1 tahun
                ''')
    st.write('Skills : Python, R, HTML, CSS')
    st.write("As a versatile data professional, I specialize in data science, data analysis, data engineering, front-end development, and computer vision. With expertise in Python, R, JavaScript, React, HTML, CSS, Power BI, Tableau, Excel, Spark, SQL, machine learning, and deep learning, I am well-equipped to deliver powerful insights and solutions across various domains.")
    st.write("I hold a degree in Materials and Metallurgical Engineering from the Sepuluh Nopember Institute of Technology and currently serve as a Data Scientist. Over the past years, I have completed numerous training programs focused on honing my data science skills and have contributed to several data-related projects.")
    st.write("My experience in Impala, Spark, and other cutting-edge technologies enables me to deliver high-quality solutions that drive business success. I am passionate about using data to inform decision-making and solve complex business challenges. I thrive in fast-paced, collaborative environments and am always looking for new opportunities to learn and grow in my field.")
    
    st.subheader('Contanct :')
    st.write('Email : zen@example.com')

    st.subheader('Nomor HP')
    st.write('Contact WA : +6235123561283')



if __name__ == '__main__':
    main()
