import streamlit as st

st.set_page_config(
    page_title="Performance Measures",
    page_icon='📈'
)

st.title('About the method')
cont = st.container()
cont2 = st.container()

cont3 = st.container()
cont4 = st.container()


cont.markdown('<div style="text-align: justify;">The article titled "A state-of-the-art survey of evaluation based on distance from average solution (EDAS): Developments and applications" by Torkayesh, Deveci, Karagoz, and Antucheviciene (2023) provides a comprehensive overview of the EDAS method and its advancements and applications. The authors conduct a literature review to examine the developments and extensions of the EDAS method since its inception in 2015. They explore various studies and publications related to EDAS, considering factors such as publication year, authorship, author countries, journals, and combined methods and uncertainty sets. The article presents a theoretical review of relevant studies, highlighting the key findings and contributions in the field. It also includes a meta-analysis of the identified literature, providing insights into the trends and patterns observed in the research on EDAS. Furthermore, the authors categorize the practical applications of the EDAS method into nine distinct groups, namely agriculture, business management, construction management, energy and natural resources, healthcare management, information technology (IT), manufacturing, supply chain management, and transportation management. This categorization offers a comprehensive understanding of how EDAS is being utilized in various domains. Overall, the article serves as a valuable resource for researchers, practitioners, and decision-makers interested in the EDAS method. It presents a state-of-the-art survey, consolidating the developments, extensions, and applications of EDAS, thereby contributing to the existing body of knowledge in this field.</div>', unsafe_allow_html=True)
cont2.markdown('<div style="text-align: justify;">Reference:</div>', unsafe_allow_html=True)
cont3.markdown('<div style="text-align: justify;">Torkayesh, A. E., Deveci, M., Karagoz, S., & Antucheviciene, J. (2023). A state-of-the-art survey of evaluation based on distance from average solution (EDAS): Developments and applications. Expert Systems with Applications, 119724.</div>', unsafe_allow_html=True)
 

url = "https://doi.org/10.1016/j.eswa.2023.119724"
cont4.write("[https://doi.org/10.1016/j.eswa.2023.119724](%s)" % url)
