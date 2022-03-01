#   Coded by D4n13l3k00    #

#     t.me/D4n13l3k00      #

# This code under AGPL-3.0 #

import os

import random

import string

from .. import loader, utils

@loader.tds

class VSHAKALMod(loader.Module):

    strings = {"name": "Photo Shakal"}

    @loader.owner

    async def vshcmd(self, m):

        ".vsh <реплай на фото> <уровень от 1 до 6 (по умолчанию 3)>\

        \nСшакалить фото"

        reply = await m.get_reply_message()

        if not reply:

            return await m.edit("reply...")

        if reply.file.mime_type.split("/")[0] != "photo":

            return await m.edit("shit...")

        args = utils.get_args_raw(m)

        lvls = {

            "1": "0.1M",

            "2": "0.08M",

            "3": "0.05M",

            "4": "0.03M",

            "5": "0.02M",

            "6": "0.01M"

        }

        if args:

            if args in lvls:

                lvl = lvls[args]

            else:

                return await m.edit("не знаю такого")

        else:

            lvl = lvls["3"]

        await m.edit("[Шакал] Качаю...")

        vid = await reply.download_media(

            "".join(random.choice(string.ascii_letters) for i in range(25))

            + ".png"

        )

        out = (

            "".join(random.choice(string.ascii_letters) for _ in range(25))

            + ".png"

        )

        await m.edit("[Шакал] Шакалю...")

        os.system(

            f"ffmpeg -y -i \"{pic}\" -b:v {lvl} -maxrate:v {lvl} -b:a {lvl} -maxrate:a {lvl} \"{out}\"")

        await m.edit("[Шакал] Отправляю...")

        await reply.reply(file=out)

        await m.delete()

        os.remove(vid)

        os.remove(out)
