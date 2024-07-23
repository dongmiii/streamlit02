import streamlit as st

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

# 검색창 

# 입력창에서 데이터를 받아서 
title = st.text_input("데이터 입력 : ")
title = "몬"

# 해당 문자열이 일치하는 이미지를 화면에 출력해 보세요.
for ani_ in ani_list:
    if title in ani_:
        # ani_list에서 특정 문자열을 포함한 인덱스를 찾아서 st.image(img_list[]) 넣어줌
        img_idx = ani_list.index(ani_)

if title != '':
    st.image(img_list[img_idx])

# if (img_idx == -1) or (img_idx == None):
#     st.write('찾는 데이터가 없습니다.')
# else:
#     st.image(img_list[img_idx])


# if title == ani_list[0]:
#     st.image(img_list[0])
#     st.download_button("image", img_list[0])
# elif title == ani_list[1]:
#     st.image(img_list[1])
# elif title == ani_list[2]:
#     st.image(img_list[2])


# with open("flower.png", "rb") as file:
#     btn = st.download_button(
#             label="Download image",
#             data=file,
#             file_name="flower.png",
#             mime="image/png"
#           )

    