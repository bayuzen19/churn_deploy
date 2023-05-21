# Import library
import streamlit as st

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

#--- Function ----
st.set_option('deprecation.showPyplotGlobalUse', False)

def load_data():
    df = pd.read_csv('./telco_churn.csv')
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'],errors='coerce')
    df = df[df['tenure']>0]
    df['Churn'] = df['Churn'].replace(['Yes','No'],[1,0]).astype(int)
    return df

def bar_stack(df,col_x,col_y='Churn'):
    
    # create crosstab and normalize the values
    ct = pd.crosstab(df[col_x], df[col_y])
    ct_pct = ct.apply(lambda x: x / x.sum(), axis=1)

    # plot stacked horizontal bar chart
    ax = ct_pct.plot(kind='barh', stacked=True, color=['#1f77b4', 'red'])

    # add annotations
    for i in ax.containers:
        # get the sum of values in each container
        total = sum(j.get_width() for j in i)
        
        for j in i:
            # get the width and height of the bar
            width = j.get_width()
            height = j.get_height()
            
            # calculate the position of the text
            x = j.get_x() + width / 2
            y = j.get_y() + height / 2
            
            # format the text as percentage
            text = f'{width:.0%}'
            
            # set the position and format of the annotation
            ax.annotate(text, xy=(x, y), xytext=(0, 0), textcoords='offset points',
                        ha='center', va='center', color='white', fontsize=12,
                        fontweight='bold')

    # set plot title and labels
    ax.set_title(f'Churn Rate by {col_x}')
    ax.set_xlabel('Number of Customers')
    ax.set_ylabel(f'{col_x}')
    # # show the plot
    plt.legend(title='Churn', loc='center left', bbox_to_anchor=(1.0, 0.5))

df = load_data()

# List Pilihan

list_pilihan = ['Business Insight','Summary Statistics','EDA']

# Side bar
sidebar = st.sidebar.selectbox(
    "Pilihan",
    list_pilihan
)

#Pilihan adalah business insight
if sidebar == 'Business Insight':
    # Judul
    st.title('Problem Statement : Customer :red[Churn] Analysis')
    st.markdown('---')

    st.subheader('Business Problem')
    st.markdown('''
        - Menganalisis factor penyebab customer churn.
        - Membuat Machine learning untuk prediksi secara langsung customer yang akan churn berdasarkan factor factor.
    ''')

    st.subheader('Objective')
    st.write('- Menurukan percentase Churn')

elif sidebar == 'Summary Statistics':
    st.title('Eksploratory Data :green[Analysis]: 🎧')
    st.markdown('---')

    # Tampilkan Data
    st.subheader('Tampilan Data')
    st.dataframe(df.head())

    st.subheader('Summary Statistics')
    st.table(df.describe())

    st.write('- Pelanggan yang churn mayoritas adalah non-senior citizen (75.53%), tetapi ada sekitar 25.47% pelanggan yang churn merupakan senior citizen.')
    st.write('- Masa berlangganan (tenure) pelanggan churn memiliki nilai rata-rata yang relatif rendah (17.98 bulan), artinya mayoritas pelanggan yang churn telah menggunakan layanan selama kurang dari 2 tahun.')
    st.write('- Biaya bulanan (monthly charges) pelanggan churn memiliki rata-rata yang relatif rendah (74.44 dollar), namun dengan standar deviasi yang cukup tinggi (24.67 dollar), sehingga ada pelanggan churn dengan biaya bulanan yang sangat rendah (18.85 dollar) atau sangat tinggi (118.35 dollar).')
    st.write('- Total biaya (total charges) pelanggan churn memiliki rata-rata yang cukup tinggi (1531.80 dollar), namun dengan standar deviasi yang cukup tinggi juga (1890.82 dollar), sehingga ada pelanggan churn dengan total biaya yang sangat rendah (18.85 dollar) atau sangat tinggi (8684.80 dollar).')

elif sidebar == 'EDA':
    st.title('EDA')

    # List Pilihan EDA
    list_eda = ['line chart','bar chart','Correlation']

    sidebar_eda = st.sidebar.selectbox(
        'List EDA',
        list_eda
    )

    if sidebar_eda == 'line chart':
        st.subheader('EDA : :red[% Churn] by Tenure')

        # analisa
        churn_tenur = df.groupby('tenure')['Churn'].mean()

        fig,ax = plt.subplots(figsize=(10,8))
        ax = churn_tenur.plot(linestyle='--',marker='o')
        plt.title('Churn Rate By Tenure',fontsize=14)
        plt.ylabel("Churn Rate %");

        st.pyplot(fig)
        st.write('Data menunjukkan bahwa churn rate (persentase pelanggan yang berhenti berlangganan) cenderung tinggi pada pelanggan dengan tenure rendah.')
        st.write('- Pelanggan dengan tenure 1 memiliki churn rate tertinggi yaitu 61,99%.')
        st.write('Terdapat kemungkinan bahwa pelanggan dengan tenure rendah dan churn rate tinggi kebanyakan berasal dari kontrak bulanan, karena pelanggan yang berlangganan kontrak bulanan cenderung lebih mudah untuk berhenti berlangganan jika mereka tidak puas dengan layanan yang diberikan. Namun, hal ini masih perlu diperiksa dengan memeriksa data mengenai kontrak yang dipilih oleh pelanggan yang churn.')

    elif sidebar_eda == 'bar chart':
        # Contract Analysis
        st.pyplot(bar_stack(df,'Contract'))
        st.write('Terlihat bahwa pelanggan yang memiliki kontrak bulanan (month-to-month) memiliki churn rate yang jauh lebih tinggi dibandingkan dengan pelanggan yang memiliki kontrak satu tahun atau dua tahun. Lebih dari setengah (57.29%) dari pelanggan dengan kontrak bulanan berhenti berlangganan (churn), sedangkan pelanggan dengan kontrak satu tahun dan dua tahun memiliki churn rate yang jauh lebih rendah, yakni masing-masing 11.28% dan 2.85%. Hal ini menunjukkan bahwa pelanggan dengan kontrak bulanan cenderung lebih tidak setia dan lebih mudah untuk berhenti berlangganan')

        col1,col2 = st.columns(2) # membuat 2 colom

        with col1:
            st.pyplot(bar_stack(df,'SeniorCitizen'))
            st.write('Terlihat bahwa pelanggan dengan status tinggi (Senior Citizen) memiliki churn rate yang jauh lebih tinggi dibandingkan dengan pelanggan dengan status rendah')

        with col2:
            st.pyplot(bar_stack(df,'gender'))
            st.write('Terlihat bahwa Gender tidak memiliki pengaruh terhadap Churn')
    
    elif sidebar_eda =='Correlation':
        st.subheader('Correlation Variable')

        col21, col22 = st.columns(2)

        with col21:
            st.write(':blue[**Correlation Pearson**] (❁´◡`❁)')

            # Korelasi pearson
            df_pearson = df.corr()
            mask = np.triu(np.ones_like(df_pearson, dtype=bool))

            fig,ax = plt.subplots(figsize=(10,10))
            # ax = sns.heatmap(df_pearson, mask=mask, cmap='coolwarm', square=True, annot=True, cbar_kws={'shrink':.5})
            ax = sns.heatmap(df_pearson,mask=mask,cmap='coolwarm',vmin=-1,vmax=1,annot=True)

            st.pyplot(fig)
            
            
        with col22:
            st.write(':blue[**Correlation Spearman**] (❁´◡`❁)')
             # Korelasi pearson
            df_spearman = df.corr(method='spearman')
            mask = np.triu(np.ones_like(df_spearman, dtype=bool))

            fig,ax = plt.subplots(figsize=(10,10))
        # ax = sns.heatmap(df_pearson, mask=mask, cmap='coolwarm', square=True, annot=True, cbar_kws={'shrink':.5})
            ax = sns.heatmap(df_pearson,mask=mask,cmap='coolwarm',vmin=-1,vmax=1,annot=True)
            st.pyplot(fig)
        
        st.markdown('''Churn Berkolerasi Medium dengan Tenure dengan Arah Negatif,
                      Artinya ketika customer itu lama dengan company maka kemungkinan churn akan semakin kecil''')






