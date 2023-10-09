from pyrogram import Client, filters
from pyrogram.types import Message
from youtube_search import YoutubeSearch
from pyrogram.types import InputMediaPhoto
from pyrogram import InlineKeyboardButton, InlineKeyboardMarkup
import requests

api_id = '21846639'  # Replace with your API ID
api_hash = '2cebc99bd8378b5237b31ea8e7496d79'  # Replace with your API hash
bot_token = '6646872835:AAHVwzim5aG4RSBgiLsUNCRi8ILgmCCrglo'  # Replace with your bot token

app = Client('VILLIAN PLAYER', api_id, api_hash, bot_token=bot_token)

@app.on_message(filters.command('start'))
def start_command_handler(client: Client, message: Message):
    # Send the advertising text
    text = "ʜᴇʏ 𝓑𝓪𝓫𝔂, 🥀
๏ ᴛʜɪs ɪs 𝐀𝐍𝐒𝐇𝐈𝐊𝐀 ✘ 𝐁𝐎𝐓 !

➻ ᴀ ғᴀsᴛ ᴀɴᴅ ᴘᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ."

    # Send the photo using the JPG image URL
    photo_url = 'https://graph.org/file/3ab2901650851a2c747aa.jpg'
    photo_caption = text  # Concatenate the advertising text with the photo caption
    response = requests.get(photo_url)  # Fetch the photo from the URL
    photo_data = response.content  # Get the binary data of the photo
    client.send_photo(chat_id=message.chat.id, photo=photo_data, caption=photo_caption)

    # Create and send the group buttons
    button1 = InlineKeyboardButton('🌷𝙐𝙥𝙙𝙖𝙩𝙚𝙨🌷', url='https://t.me/vilen_3r')
    button2 = InlineKeyboardButton('🏵️𝙎𝙪𝙥𝙥𝙤𝙧𝙩🏵️', url='https://t.me/villen_012')
    reply_markup = InlineKeyboardMarkup([[button1], [button2]])
    client.send_message(chat_id=message.chat.id, text="𝑱𝒐𝒊𝒏 𝒐𝒖𝒓 𝒎𝒖𝒔𝒊𝒄 𝒈𝒓𝒐𝒖𝒑𝒔:", reply_markup=reply_markup)


@app.on_message(filters.command('play'))
def play_command_handler(client: Client, message: Message):
    # Get the song name from the command message
    song_name = ' '.join(message.command[1:])

    # Search for the song on YouTube
    results = YoutubeSearch(f'{song_name} official audio', max_results=1).to_dict()
    if len(results) > 0:
        video_title = results[0]['title']
        video_thumbnail = results[0]['thumbnails'][0]
        video_url = f"https://www.youtube.com/watch?v={results[0]['id']}"
    else:
        client.send_message(message.chat.id, f"No results found for '{song_name}'")
        return

    # Join the voice chat
    voice_chat = message.chat.voice_chat
    if voice_chat:
        voice_chat.join()

    # Send the audio and video details to the voice chat
    client.send_message(
        chat_id=message.chat.id,
        text=f"<b>𝙉𝙤𝙬 𝙥𝙡𝙖𝙮𝙞𝙣𝙜:</b>\n{video_title}",
        reply_markup=InputMediaPhoto(
            media=video_thumbnail
        ),
        parse_mode='html'
    )
    client.send_audio(
        chat_id=message.chat.id,
        audio=video_url,
        title=song_name
    )

app.run()
