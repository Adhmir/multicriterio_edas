import streamlit as st


st.set_page_config(
    page_title="ApoioDecisao",
    page_icon='📈'
)


st.title('How cite us')
cont1 =st.container()
cont1.write('Gomes, A. R. V. & Hein, N. (2023). Multiple Criteria Perfomance Measures - EDAS [Web streamlit app]. https://decisionsupport-adriana.streamlit.app/')

            
st.subheader('About the Authors')
col1, col2 = st.columns(2)
col1.write('- PhD Canditate Adhmir Renan Voltolini Gomes')
col1.write('arvgomes@furb.br')
col1.write("Currently pursuing a Doctorate in Accounting and Administration at the esteemed Regional University of Blumenau, holds a Master's degree in Accounting from the esteemed State University of West Paraná. Additionally, have specialized in Financial Management, Accounting, and Controllership (Inbrape). Their academic journey commenced with a Bachelor's degree in Administration from the esteemed Union of Education of Cascavel. Notably, actively contributes as member of the Research Group in Financial Accounting and Finance within the renowned Stricto-Sensu Postgraduate Program in Accounting (PPGC). Their areas of expertise encompass Finance, Environmental Turbulence, Controllership, Corporate Governance, and the application of Multivariate Models to the realm of Finance.")
col2.write('- Profº Dr. Nelson Hein')
col2.write('hein@furb.br')
col2.write("Graduated in Science in 1987 and in Mathematics in 1988 from the Regional University of Blumenau - FURB. He also holds a specialization in Science/Mathematics Education from the same university in 1990. Professor Hein continued his studies and obtained a Master's degree in Production Engineering in 1994 and a Ph.D. in Production Engineering in 1998 from the Federal University of Santa Catarina (UFSC). He also conducted post-doctoral research at the National Institute of Pure and Applied Mathematics (IMPA) in 2003 and at the Anderson School of Management at the University of New Mexico, USA, completing it in 2011. Since 1989, Dr. Nelson Hein has been a professor in the Mathematics Department at the Regional University of Blumenau. He is currently a permanent professor in the Postgraduate Program in Accounting Sciences (PPGCC) at the same university. He has conducted research on productivity (PQ2) from 2011 to 2019. Professor Hein is also the current coordinator of DINTER PPGCC/FURB - UFF (Macaé). He has experience in the field of Applied Mathematics, with a focus on multivariate statistical analysis and multi-criteria decision analysis. He coordinates the MULTIVAR Study Group, affiliated with the Spanish Group for Multicriteria Decision Making (GEDM).")
st.subheader('About the Institution')


st.subheader("Stricto-Sensu Postgraduate Program in Accounting (PPGC) - FURB")
st.markdown("The Stricto-Sensu Postgraduate Program in Accounting (PPGC) is a distinguished academic program offered by the Regional University of Blumenau (FURB). Designed for individuals seeking advanced knowledge and specialization in the field of Accounting, the PPGC provides a comprehensive curriculum that fosters intellectual growth and research excellence.")
# Add a link to the program's webpage
st.markdown("[Click here](https://www.furb.br/web/1854/cursos/programa-pos-graduacao/ciencias-contabeis/apresentacao) for more information about the PPGC.")
# Add more details and highlights about the program
st.subheader("Program Highlights")
st.markdown("- Develops highly skilled professionals in accounting.")
st.markdown("- Rigorous coursework and research activities.")
st.markdown("- Faculty of renowned experts and experienced researchers.")
st.markdown("- Focus on critical thinking, innovation, and scholarly exploration.")
st.markdown("- Broad curriculum covering various areas of accounting.")
st.markdown("- Encourages interdisciplinary collaboration and partnerships.")
st.markdown("- Opportunities for practical research projects and industry engagement.")

# Conclusion
st.markdown("Through its commitment to excellence and a rigorous academic approach, the Stricto-Sensu Postgraduate Program in Accounting (PPGC) at the Regional University of Blumenau (FURB) stands as a distinguished platform for aspiring accounting professionals to acquire advanced knowledge, contribute to research, and make significant contributions to the field of accounting.")

st.subheader("Contact Information")
st.markdown('Fundação Universidade Regional de Blumenau, Blumenau - Santa Catarina - Brasil')
st.markdown('Rua Antônio da Veiga, 140 - Itoupava Seca. Zip code: 89030-903')
st.markdown("Campus 1: D-202")
st.markdown("Phone: 47 3321-0565")
st.markdown("Email: ppgcc-doutorado@furb.br")