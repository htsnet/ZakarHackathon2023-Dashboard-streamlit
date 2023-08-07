import streamlit as st

st.set_page_config(page_title='Save Zakar Hackathon', 
                   page_icon='🚗', layout='centered', initial_sidebar_state='expanded' )

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
        st.image('logo-250-transparente.png')
        st.header('Information')
        st.write("""
                A fictional island nation named Zakar is suffering from wildfires. 
                Let's help them build an early warning system and save lives and earth!
                """)
        
        st.header('About')
        st.write('Details about this project can be found in ')
        
        
    # definition
    ttl = 100000     # long time, the dataset is almost fixed


    # título
    title = f'Traffic Violations'
    st.title(title)
    
    subTitle = f'A partial view of traffic violation tickets from São Caetano do Sul'
    st.subheader(subTitle)

    #connection with the MySQL with data
    conn = st.experimental_connection("violations_db", type='sql')

    # information tabs
    tab1, tab2, tab3, tab4 = st.tabs(['Summary', 'Code', 'Date', 'Champions'])


    # show tabs to choose the action
    with tab1:
        botSummary = st.button("Click to make a summary of the content")
        if botSummary:
            summary = conn.query("""
                            select COUNT(*) AS Qty
                            from CEN_tInfracoes
                            """, ttl=ttl)
            st.write('Total records found: ', str(summary['Qty'][0]))
                    

    with tab2:    
        botCode = st.button("Click to get the quantity of each violation code")
        if botCode:
            code = conn.query("""
                            select InfracoesCodigo as 'Violation Code',  COUNT(*) AS Qty
                            from CEN_tInfracoes
                            group by InfracoesCodigo
                            order by Qty desc 
                            """, ttl=ttl)
            st.write(code) 

            
    with tab3:        
        botDate = st.button("Click to get the quantity of date")
        if botDate:
            date = conn.query("""
                            select InfracoesDataInfracao,  COUNT(*) AS Qty
                            from CEN_tInfracoes
                            group by InfracoesDataInfracao
                            order by InfracoesDataInfracao 
                            """, ttl=ttl)
            st.write(date) 


    with tab4:        
        botChampions = st.button("Click to get the violation champions")
        if botChampions:
            champions = conn.query("""
                            select InfracoesPlaca as 'Plate',  COUNT(*) AS Qty
                            from CEN_tInfracoes
                            group by InfracoesPlaca
                            Having Qty > 5
                            order by Qty desc 
                            """, ttl=ttl)
            st.write(champions) 
            st.write('Listing only Qty > 5')

if __name__ == '__main__':
	main()   