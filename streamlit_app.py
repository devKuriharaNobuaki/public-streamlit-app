#!/usr/bin/env -S python -m streamlit run

import streamlit as st

st.caption('キャプション `<caption>`')

st.text('''
ここに書いたことが表示される。
これは、public設定なので注意すること。
''')

st.code('''
import streamlit as st
st.show()''',
    language='python',
    line_numbers=True)
