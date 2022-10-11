import streamlit as st
import util

def main():
  key = [5, 7] 
  y =0
  enc_text = util.encrypt(pesan, key)
  st.header('Plain Text')
  st.write('Decrypted Text: {}'.format(util.decrypt(enc_text, key) ))
  st.header('Affine Chiper Text')
  st.write('Encrypted Text: {}'.format(enc_text)) 

 
  
  ##print("errors : ",y)

               

        
     
    
if __name__ == '__main__':
    st.title("Program Encryption and Decryption Affine Chiper")
    form = st.form(key='my-form')
    pesan = form.text_input('Silakan Masukan Text Anda)', '-')
    submit = form.form_submit_button('Generate')
    
   
    if submit:
        main()
       
                        
    
     
