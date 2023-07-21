import streamlit as st
import os
from dotenv import load_dotenv
import sys
import pandas as pd

st.set_page_config(
        page_title="Content Generation",
        layout="wide",
)
# st.write(os.getcwd())
# sys.path.append(os.path.join(os.getcwd(),'/server/scripts'))

sys.path.append(os.path.join(os.getcwd(), 'server/scripts'))

from createTopic import generateTopicList

## SET WORKING DIRECTORY TO ../server/scripts

# st.write(os.getenv("OPENAI_API_KEY"))


with st.form("Generate a Topic List"):
    st.write("Generate a structured list based on a topic and location")
    topic = st.text_input("Topic")
    location = st.text_input("Location")

    file_path= os.path.join(os.getcwd(), 'server/scripts/scriptfiles/topics/')
    # st.write(file_path)
    submit_button = st.form_submit_button(label='Create List')
    if submit_button:
        topic_list = generateTopicList(topic, location, 10, save=True, path=file_path)
        st.write(topic_list)



sidebar = st.sidebar.container()

with sidebar.empty():
    topic_directory = "server/scripts/scriptfiles/topics/"
    topic_files = os.listdir(topic_directory)
    topic_files = [file.split('_')[0] + '/' + file.split('_')[1] for file in topic_files if file.endswith(".csv")]
    if len(topic_files) > 0:
        st.write("Previously Generated Topic Lists")
        # st.write(topic_files)
        st.write("Select a topic to view the list")
        selected_topic_location = st.selectbox("Topic/Location", topic_files)
        # topic_df = pd.read_csv(f"{topic_directory}{selected_topic}_list.csv")
        # st.write(topic_df)

# if 'topic_list' not in st.session_state:
#     st.session_state.topic_list = []

def add_topic(new_topic_item: str):
    if new_topic_item in st.session_state.topic_list or new_topic_item in st.session_state.topic_df[selected_topic].to_list():
        st.empty().error(f"{new_topic_item} already in the list")

        with st.empty():
            if st.button("Do you want to remove it?"):
                # st.session_state.topic_list.remove(new_topic_item)
                st.session_state.topic_df = st.session_state.topic_df[st.session_state.topic_df[selected_topic] != new_topic_item]
                st.session_state.topic_df.to_csv(f"{topic_directory}{selected_topic}_{selected_location}_list.csv")
                st.success(f"{new_topic_item} removed from the list")
                output.write(st.session_state.topic_df)
    else:
        index = len(st.session_state.topic_df)
        st.session_state.topic_list.append(new_topic_item)
        st.success(f"{new_topic_item} added to the list")
        st.session_state.topic_df = pd.concat([st.session_state.topic_df, pd.DataFrame({
            'Index': [index],
            selected_topic: [new_topic_item]}).set_index("Index")]
                )
        st.session_state.topic_list = []
        st.session_state.topic_df.to_csv(f"{topic_directory}{selected_topic}_{selected_location}_list.csv")            
        output.write(st.session_state.topic_df)
        
st.divider()

if selected_topic_location:
    selected_topic = selected_topic_location.split('/')[0]
    selected_location = selected_topic_location.split('/')[1]
    selected_topic_location_reformat = selected_topic_location.replace('/', '_')
    st.session_state.topic_df = pd.read_csv(f"{topic_directory}{selected_topic}_{selected_location}_list.csv", index_col="Index")
    st.session_state.menu_options = st.session_state.topic_df[selected_topic].to_list()

    # edited_topic_df = st.data_editor(
    #     topic_df,
    #     num_rows="dynamic",
    #     key="topic_df",
    #     hide_index=False,
    # )
    edit_topic_list, generate_subtopic = st.tabs(["Edit Topic List", "Generate Sub-Topics"])

    with edit_topic_list:
        new_topic_item = st.text_input("Add a new topic item to the list", key="new_topic_item")
        
        output = st.empty()
        output.write(st.session_state.topic_df)
        
        if 'topic_list' not in st.session_state:
            st.session_state.topic_list = []

        if new_topic_item:
            add_topic(new_topic_item)

        
    # save_topic_confirm = st.button("Save Topic List", key="save_topic_list", on_click=add_topic, args=(new_topic,))

        # for i, topic in enumerate(st.session_state.topic_list):
        #     st.write(i)

        # index = len(topic_df) 


        # topic_df = pd.concat([topic_df, pd.DataFrame({
        #     'Index': [index],
        #     selected_topic: new_topic}).set_index("Index")])
    


    #     st.session_state.topic_list

    # st.write(st.session_state.topic_list.values)
        # topic_df = pd.concat([topic_df, pd.DataFrame({
        #     'Index': [index],
        #     selected_topic: topic_list}).set_index("Index")])
            
        # output.write(topic_df)
