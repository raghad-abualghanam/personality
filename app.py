import streamlit as st 
import joblib
model = joblib.load(r"Untitled folder\personality_model.pk1")
st.title("Personality_predictor")
time_alone = st.number_input("Time spent alone" 
                            , min_value=0,
                            max_value=11,
                            step=1
)
stage_fear = st.selectbox("stage fear", ["No", "Yes"])
social_events = st.number_input("Social event attendance"
                                ,min_value=0,
                               max_value=10,
                               step=1
)
going_outside = st.number_input("Going outside"
                               ,min_value=0, 
                                max_value=7,
                                step=1
)
drained = st.selectbox("Drained after socialization", ["No","Yes"])
friends = st.number_input("Friends circle size" 
                          ,min_value=0, 
                           max_value=15 , 
                          step=1
)
post_frequency = st.number_input("Post frequency", min_value=0,
                                max_value=10, 
                                 step=1)
if st.button("Predict"):
    stage_fear_value = 1 if stage_fear == "Yes" else 0
    drained_value = 1 if drained == "Yes" else 0
    new_person = [[
        time_alone,
        stage_fear_value,
        social_events,
        going_outside,
        drained_value,
        friends,
        post_frequency
]]
    prediction = model.predict(new_person)
    if prediction[0] == 1:
      st.success("Extrovert")
    
    else:
     st.info("Introvert")