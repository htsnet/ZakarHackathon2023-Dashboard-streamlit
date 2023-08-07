import streamlit as st

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
        st.image('island.jpg')
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
    title = f'Save Zakar'
    st.title(title)
    
    subTitle = f'Some aspects and facts about Zakar'
    st.subheader(subTitle)

    # information tabs
    tab1, tab2, tab3, tab4 = st.tabs(['Wildfires', 'Code', 'Date', 'Champions'])


    # show tabs to choose the action
    with tab1:
        st.write("""
                Here we can see the register of wildfires in the last 7 years.
                This map represents all geographic coordinates of the island. 
                """)
        st.image('wildfires_map.png')
                    

    with tab2:    
        botCode = st.button("Click to")
        if botCode:
            pass

            
    with tab3:        
        botDate = st.button("Click to ")
        if botDate:
            pass 


    with tab4:        
        botChampions = st.button("Click to ")
        if botChampions:
            pass

if __name__ == '__main__':
	main()   