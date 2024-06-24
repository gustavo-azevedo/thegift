from config.general_config import firebaseConfig, get_auth_client, get_db, get_firebase
import streamlit as st
auth = get_auth_client()
db = get_db()
auth_client = get_auth_client()
firebase = get_firebase()
# Function to check if a user is new
def is_new_user(user_id):
    user_ref = db.collection('users').document(user_id)
    user_doc = user_ref.get()
    return not user_doc.exists

def needs_onboarding(user_id):
    user_ref = db.collection('users').document(user_id)
    user_doc = user_ref.get()
    if user_doc.exists:
        user_data = user_doc.to_dict()
        return not user_data.get('onboarded', False)
    return True

def show_onboarding(user_id):
    onboarding_steps = [
        ("Antes de começarmos, queremos te conhecer melhor. Vamos começar?", None),
        ("Qual o tamanho de roupa você usa?", ["PP", "P", "M", "G", "GG", "XG"]),
        ("Qual o seu estilo?", ["casual", "streetware", "formal"]),
        ("Quais seus principais interesses?", ["roupas", "skin care", "Eletronicos"]),
        ("Quais tecidos você prefere?", ["algodao", "poliester", "cetim"]),
        ("Seu perfil está pronto! Agora você pode indicar seus produtos preferidos.", None),
    ]

    if 'current_step' not in st.session_state:
        st.session_state.current_step = 0
    current_step = st.session_state.current_step
    print('current_step', st.session_state.current_step, 'onboarding_steps', len(onboarding_steps), 'var current_step', current_step)

    step_message, options = onboarding_steps[current_step]

    st.write(step_message)

    # Display the appropriate input widget based on options
    if options:
        if current_step == 1:
            selected_option = st.radio("Escolha o tamanho:", options)
        elif current_step == 2:
            selected_option = st.radio("Escolha o estilo:", options)
        elif current_step == 3:
            selected_option = st.multiselect("Escolha os interesses:", options)
        elif current_step == 4:
            selected_option = st.multiselect("Escolha os tecidos:", options)
    else:
        selected_option = None

    if st.button('Próximo'):
        if options and not selected_option:
            st.warning("Selecione ao menos uma opção para continuar.")
        else:
            if options:
                field_name = ["size", "style", "interests", "fabrics"][current_step - 1]
                db.collection('users').document(user_id).set({field_name: selected_option}, merge=True)
            st.session_state.current_step += 1
            if st.session_state.current_step >= len(onboarding_steps):
                db.collection('users').document(user_id).set({'onboarded': True}, merge=True)
                st.session_state.current_step = 0
            st.experimental_rerun()