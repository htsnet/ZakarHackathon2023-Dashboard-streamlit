import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title='Save Zakar Hackathon', 
                   page_icon='🏝', layout='centered', initial_sidebar_state='expanded' )

#para esconder o menu do próprio streamlit 
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
# passa javascript e estilos
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def main():
    with st.sidebar:
         # título
        title = f'Save Zakar'
        st.title(title)
        st.image('island.jpg', clamp=True)
        st.header('Information')
        st.write("""
                A fictional island nation named Zakar is suffering from wildfires. 
                Let's help them build an early warning system and save lives and earth!
                """)
        
        st.header('About')
        st.write('Details about this project can be found in https://github.com/htsnet/ZakarHackathon2023-Dashboard-streamlit')
        
        
    # definition
    ttl = 100000     # long time, the dataset is almost fixed


    # título
    st.title(title)
    
    subTitle = f'Some aspects and facts about Zakar'
    st.subheader(subTitle)

    # information tabs
    tab1, tab2, tab3, tab4 = st.tabs(['Wildfires', 'Alerts', 'Tweets', 'Temperature'])


    # show tabs to choose the action
    with tab1:
        st.write("""
                Here we can see the register of wildfires in the last 7 years.\n
                This map represents all geographic coordinates of the island. 
                """)
        st.image('wildfires_map.png', clamp=True)
                    

    with tab2:    
        st.write("""
                Here we can see a table wiht wildfire alerts per day in the last 7 years.
                """)
        # get original 
        df_alerts = pd.read_csv('alert_per_day.csv')
        df_alerts.columns = ['Day', 'Qty']
        
        # create a empty dataset with all dates
        df_alerts_complete = pd.DataFrame(columns=['Day', 'Qty']) 

        # fill the dataset with zeros
        limit_alerts = 2550
        for i in range(limit_alerts):
            df_alerts_complete.loc[i] = [i, 0]
            
        # update days with alerts
        df_alerts_aux = df_alerts.reset_index()
        for i, row in df_alerts_aux.iterrows():
            # st.write(row['Day'], row['Qty'])
            df_alerts_complete.loc[row['Day']] = [row['Day'], row['Qty']]
        # st.dataframe(df_alerts_complete)

        # create a new plot
        fig, ax = plt.subplots()
        plt.plot(df_alerts_complete['Day'], df_alerts_complete['Qty']) 
        plt.title('Wildfires Alerts per Day')
        plt.xlabel('Day')
        plt.ylabel('Quantity')
        plt.show()
        st.pyplot(fig)
        
        st.write("""
            Bellow you can see all records of alerts per day.
            Note that the number of alerts per day show only the days with alerts. 
        """)
        #show dataset
        df_alerts = df_alerts.set_index('Day')
        st.dataframe(df_alerts)
        
    with tab3:        
        st.write("""
                Here we can see a table with tweets per day in the last 7 years.
                """)
        df_tweets = pd.read_csv('tweets_per_day.csv')
        df_tweets.columns = ['Day', 'Qty']
        
        # create a new plot
        fig, ax = plt.subplots()
        plt.plot(df_tweets['Day'], df_tweets['Qty']) 
        plt.title('Tweets per Day')
        plt.xlabel('Day')
        plt.ylabel('Quantity')
        plt.show()
        st.pyplot(fig)
        
        st.write("""
            Bellow you can see all records of tweets per day.
        """)
        #show dataset
        df_tweets = df_tweets.set_index('Day')
        st.dataframe(df_tweets)

    with tab4:        
        st.write("""
                Here we can see a table with the average temperature per day in the last 7 years.
                """)
        df_temperatures = pd.read_csv('temperature_per_day.csv')
        df_temperatures.columns = ['Day', 'Temperature']
        
        # create a new plot
        fig, ax = plt.subplots()
        plt.plot(df_temperatures['Day'], df_temperatures['Temperature']) 
        plt.title('Average Temperature per Day')
        plt.xlabel('Day')
        plt.ylabel('Avg.Temp.')
        plt.show()
        st.pyplot(fig)
        
        st.write("""
            Bellow you can see all records of the average temperatura per day.
        """)
        #show dataset
        df_temperatures = df_temperatures.set_index('Day')
        st.dataframe(df_temperatures)

if __name__ == '__main__':
	main()   