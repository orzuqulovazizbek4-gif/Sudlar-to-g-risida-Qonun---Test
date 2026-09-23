import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="Sudlar to'g'risida Qonun - Test", page_icon="⚖️", layout="centered")

# --- TELEGRAM BOT SOZLAMALARI ---
TELEGRAM_BOT_TOKEN = "8941132517:AAFXeT3o4-jkwRz-i0PqS30LrlYl8haiQ4g"
TELEGRAM_CHAT_ID = "7628668254"

def send_telegram_notification(full_name, score, total, percentage, user_answers):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Telegram xabari (Oddiy va xavfsiz matn ko'rinishida)
    message = f"📥 YANGI TEST NATIJASI\n\n"
    message += f"👤 Talaba: {full_name}\n"
    message += f"📅 Vaqt: {now}\n"
    message += f"📊 Natija: {score} / {total}\n"
    message += f"📈 Foiz: {percentage:.1f}%\n\n"
    message += "Tanlangan javoblar:\n"
    
    for idx, ans in enumerate(user_answers, 1):
        message += f"{idx}. {ans}\n"
        
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID, 
        "text": message
    }
    
    try:
        res = requests.post(url, json=payload, timeout=10)
        res_json = res.json()
        if res.status_code == 200 and res_json.get("ok"):
            return True, "Muvaffaqiyatli"
        else:
            return False, f"Telegram API Xatosi: {res_json.get('description', res.text)}"
    except Exception as e:
        return False, f"Ulanishda xatolik: {str(e)}"

# --- TEST SAVOLLARI (I-VARIANT) ---
QUESTIONS = [
    {
        "q": "1. Quyida berilgan qaysilar O’zbekiston Respublikasi Sud tizimiga KIRMAYDI.\n1) harbiy sudlar; 2) jinoyat ishlari bo‘yicha tumanlararo, tuman, Shahar sudlari; 3) Qoraqalpog‘iston Respublikasi ma’muriy sudi, viloyatlar va Toshkent shahar ma’muriy sudlari; 4) fuqarolik ishlari bo‘yicha tuman, shahar sudlari;",
        "options": ["A) 1,3;", "B) 2,3;", "C) 1,4;", "D) 2,4;"],
        "correct": "A) 1,3;"
    },
    {
        "q": "2. XATO ma’lumotlarni aniqlang.",
        "options": [
            "A) Sudyalar korpusini shakllantirish sudyalarning mustaqilligi prinsipiga qat’iy muvofiq holda O‘zbekiston Respublikasi Sudyalar oliy kengashi tomonidan amalga oshiriladi.",
            "B) O‘zbekiston Respublikasi Konstitutsiyasiga muvofiq O‘zbekiston Respublikasi Oliy sudi o‘z vakolatlari jumlasiga kiritilgan masalalar bo‘yicha qonun loyihasini O‘zbekiston Respublikasi Oliy Majlisining Qonunchilik palatasiga kiritish orqali amalga oshiriladigan qonunchilik tashabbusi huquqiga ega.",
            "C) Sud binosida O‘zbekiston Respublikasining Davlat bayrog‘i ko‘tariladi, sud binosining old tomonida va sud majlislari zalida O‘zbekiston Respublikasi Davlat gerbining tasviri joylashtiriladi.",
            "D) Sudyalar muayyan ishlar bo‘yicha davlat statistika qo’mitasi va soliq inspeksiyasiga hisobdordir."
        ],
        "correct": "D) Sudyalar muayyan ishlar bo‘yicha davlat statistika qo’mitasi va soliq inspeksiyasiga hisobdordir."
    },
    {
        "q": "3. Quyida berilgan ma’lumotlarning nechtasi to’g’ri ekanligini toping.\n1) Sudyani muayyan ishning muhokamasidan chetlashtirishga yoki uning vakolatlarini to‘xtatib turishga... yo‘l qo‘yiladi.\n2) Qonuniy kuchga kirgan sud hujjatlari... ijro etilishi shart emas.\n3) Sud majlisi zalida... fotosuratga olishi, video va audio yozuvni amalga oshirishi taqiqlanadi.\n4) Sud ishlari yuritilayotgan tilni bilmaydigan... ona tilida so‘zlash huquqi ta’minlanadi.\n5) O‘zbekiston Respublikasi fuqarolari... sud himoyasida bo‘lish huquqiga ega.\n6) Odil sudlovni amalga oshirishda... malakali yuridik yordam olish huquqi kafolatlanadi.\n7) O‘zbekiston Respublikasi Oliy sudi Plenumi... bir oyda kamida to’rt marta chaqiriladi.",
        "options": ["A) 3 tasi to’g’ri, 4 tasi noto’g’ri;", "B) 5 tasi to’g’ri, 2 tasi noto’g’ri;", "C) 2 tasi to’g’ri, 5 tasi noto’g’ri;", "D) 4 tasi to’g’ri, 3 tasi noto’g’ri;"],
        "correct": "B) 5 tasi to’g’ri, 2 tasi noto’g’ri;"
    },
    {
        "q": "4. Quyida berilgan qaysi biri Aybsizlik prezumpsiyasiga OID EMAS.",
        "options": [
            "A) Aybdorlikka oid barcha shubhalar... gumon qilinuvchining... foydasiga hal qilinishi kerak.",
            "B) Gumon qilinuvchi... o‘zining aybsizligini isbotlashi shart emas...",
            "C) Agar shaxsning o‘z aybini tan olganligi unga qarshi yagona dalil bo‘lsa... jazoga tortilishi mumkin emas.",
            "D) Hech kim Bsoh prorkuroning qaroriga asoslanmagan holda hibsga olinishi, ushlab turilishi, qamoqqa olinishi, qamoqda saqlanishi yoki uning ozodligi boshqacha tarzda cheklanishi mumkin emas."
        ],
        "correct": "D) Hech kim Bsoh prorkuroning qaroriga asoslanmagan holda hibsga olinishi, ushlab turilishi, qamoqqa olinishi, qamoqda saqlanishi yoki uning ozodligi boshqacha tarzda cheklanishi mumkin emas."
    },
    {
        "q": "5. To’g’ri ko’rsatilgan ma’lumotni aniqlang.\n1) Hibsga olishga... vasiylik va homiylik organing qaroriga ko‘ra yo‘l qo‘yiladi.\n2) Shaxs sudning qarorisiz qirq sakkiz soatdan ortiq muddat ushlab turilishi mumkin emas.\n3) Hech kim qiynoqqa solinishi... jazoga duchor etilishi mumkin emas.\n4) Taraflar... sud hujjati ustidan shikoyat qilish huquqiga emas va bu taqiqlanadi.",
        "options": ["A) 1,3;", "B) 2,3;", "C) 1,4;", "D) 2,4;"],
        "correct": "B) 2,3;"
    },
    {
        "q": "6. Jinoyat sodir etganlikda ayblanayotgan shaxs qaysi holatgacha aybsiz deb hisoblanadi.\n1) shikoyat bildirmaguncha;\n2) uning aybi qonunda nazarda tutilgan tartibda oshkora sud muhokamasi yo‘li bilan isbotlanmaguncha;\n3) sudning qonuniy kuchga kirgan hukmi bilan aniqlanmaguncha;\n4) Plenum majlisidagi imzolangan qaror kuchga kirmaguncha;",
        "options": ["A) 1,3;", "B) 2,3;", "C) 1,4;", "D) 2,4;"],
        "correct": "B) 2,3;"
    },
    {
        "q": "7. Quyida berilgan qaysi biri O‘zbekiston Respublikasi Oliy sudi Plenumi ish YURITMAYDI.",
        "options": [
            "A) O‘zbekiston Respublikasi Oliy sudi sudyalari,",
            "B) Qoraqalpog‘iston Respublikasi sudi;",
            "C) Qoraqalpog‘iston Respublikasi ma’muriy sudi raislari;",
            "D) Qoraqalpog‘iston Respublikasi fuqarolik va jinoiy sudi rayosati rahbari;"
        ],
        "correct": "A) O‘zbekiston Respublikasi Oliy sudi sudyalari,"
    },
    {
        "q": "8. Quyida berilgan qaysilar O‘zbekiston Respublikasi Oliy sudi Plenumining majlislarida ishtirok etishi mumkin.\n1) Konstitutsiyaviy sud raisi, 2) Qonunchilik palatasi spikeri, 3) Sudyalar oliy kengashi raisi, 4) Advokatlar rayosati, 5) Bosh prokuror, 6) Ijtimoiy fikr jamoatchilik markazi, 7) Adliya vaziri;",
        "options": ["A) 1,3,5,6,7;", "B) 1,3,5,7;", "C) 2,3,5,6;", "D) 2,4,5,6,7;"],
        "correct": "B) 1,3,5,7;"
    },
    {
        "q": "9. Quyida berilgan O‘zbekiston Respublikasi Oliy sudi Plenumining majlislarida ishtirok etish huquqiga ega subyektlar qaysi qatorda XATO ko’rsatilgan.",
        "options": [
            "A) O‘zbekiston Respublikasi Oliy Majlisining Inson huquqlari bo‘yicha vakili (ombudsman),",
            "B) O‘zbekiston Respublikasi Oliy Majlisining Bola huquqlari bo‘yicha vakili (Bolalar ombudsmani),",
            "C) O‘zbekiston Respublikasi Prezidenti huzuridagi Tadbirkorlik subyektlarining huquqlari va qonuniy manfaatlarini himoya qilish bo‘yicha vakil;",
            "D) O‘zbekiston Respublikasi Prezidenti huzuridagi Fuqarolik masalalari bo’yicha maxsus komissiya;"
        ],
        "correct": "D) O‘zbekiston Respublikasi Prezidenti huzuridagi Fuqarolik masalalari bo’yicha maxsus komissiya;"
    },
    {
        "q": "10. XATO ma’lumot berilgan javobni aniqlang.",
        "options": [
            "A) Qonunchilikni qo‘llash masalalariga doir qarorlar loyihalari Plenum a’zolariga majlisdan yigirma kun ilgari yuboriladi.",
            "B) Oliy sud Plenumining qarori majlisda ishtirok etayotgan a’zolarning ko‘pchilik ovozi bilan ochiq ovoz berish orqali qabul qilinadi.",
            "C) Oliy sud Plenumining qarori qabul qilingan kundan e’tiboran qonuniy kuchga kiradi va rasmiy nashrlarda e’lon qilinadi.",
            "D) O‘zbekiston Respublikasi Oliy sudi Plenumining majlislarida ajrim va hukum asosida doimiy ishlar yuritiladi."
        ],
        "correct": "D) O‘zbekiston Respublikasi Oliy sudi Plenumining majlislarida ajrim va hukum asosida doimiy ishlar yuritiladi."
    },
    {
        "q": "11. Quyida berilgan kimlar tomonidan O‘zbekiston Respublikasi Oliy sudi Plenumi majlisining bayonnomasi imzolanmaydi.\n1) O‘zbekiston Respublikasi Oliy sudi raisi; 2) Konstitutsiyaviy sud raisi; 3) O‘zbekiston Respublikasi Oliy Majlisining Inson huquqlari bo‘yicha vakili; 4) O‘zbekiston Respublikasi Oliy sudi Plenumining kotibi;",
        "options": ["A) 1,3;", "B) 2,3;", "C) 1,4;", "D) 2,4;"],
        "correct": "B) 2,3;"
    },
    {
        "q": "12. Quyida berilgan qaysilar O‘zbekiston Respublikasi Oliy sudi Plenumi tomonidan o‘z vakolatlariga kiritilgan masalalarni ko‘rib chiqish tartibiga oid EMAS.",
        "options": [
            "A) O‘zbekiston Respublikasi Oliy sudining Plenumi ko‘rib chiqishi uchun masalalar O‘zbekiston Respublikasi Konstitutsiyaviy sud raisi tomonidan kiritiladi.",
            "B) Sudyalar oliy kengashi, Bosh prokurori tushuntirishlar berilishi haqida takliflar kiritishga haqli.",
            "C) Masalani ko‘rib chiqish Oliy sud sudyasining ma’ruzasini eshitishdan boshlanadi.",
            "D) Plenum tushuntirishlari sudlar, davlat organlari va mansabdor shaxslar uchun majburiydir."
        ],
        "correct": "A) O‘zbekiston Respublikasi Oliy sudining Plenumi ko‘rib chiqishi uchun masalalar O‘zbekiston Respublikasi Konstitutsiyaviy sud raisi tomonidan kiritiladi."
    },
    {
        "q": "13. Oliy sudi Plenumining kotibiga tegishli bo’lgan ma’lumotni aniqlang.\n1) O‘zbekiston Respublikasi Oliy sudi sudyasi vazifalarini bajarish bilan birga majlisni tayyorlash va bayonnoma yuritishni ta’minlaydi;\n2) Oliy sud raisi va o'rinbosarlarini lavozimga tasdiqlaydi;\n3) majlislari zaruriyatga qarab, har oyda kamida bir marta o‘tkazilishni ta’minlaydi;\n4) Plenum qarori ijrosini tashkil etish uchun zarur bo‘lgan harakatlarni amalga oshiradi.",
        "options": ["A) 1,3;", "B) 2,3;", "C) 1,4;", "D) 2,4;"],
        "correct": "C) 1,4;"
    },
    {
        "q": "14. Qoraqalpog‘iston Respublikasi sudi, viloyat, Toshkent shahar sudi tarkibi XATO berilgan qatorni aniqlang.",
        "options": [
            "A) Yuridik ishlari bo‘yicha sudlov palatasi;",
            "B) Fuqarolik ishlari bo‘yicha sudlov hay’ati;",
            "C) Jinoyat ishlari bo‘yicha sudlov hay’ati;",
            "D) Iqtisodiy ishlar bo‘yicha sudlov hay’ati;"
        ],
        "correct": "A) Yuridik ishlari bo‘yicha sudlov palatasi;"
    },
    {
        "q": "15. Qoraqalpog‘iston Respublikasi sudi, viloyat, Toshkent shahar sudining rayosati haqida to’g’ri berilgan qatorni aniqlang.",
        "options": [
            "A) Qoraqalpog‘iston Respublikasi sudi, viloyat, Toshkent shahar sudi rayosati shu sudning sudyalaridan iborat tarkibda ish yuritadi.",
            "B) Rayosat majlislari to’rt oyda kamida bir marta o‘tkaziladi.",
            "C) Rayosat a’zolarining uchdan bir qismi hozir bo‘lgan taqdirda vakolatlidir.",
            "D) Rayosat qarorlari Bosh prokuror tomonidan imzolanadi."
        ],
        "correct": "A) Qoraqalpog‘iston Respublikasi sudi, viloyat, Toshkent shahar sudi rayosati shu sudning sudyalaridan iborat tarkibda ish yuritadi."
    },
    {
        "q": "16. Sudya huquqbuzarlik sodir etganlikda gumon qilinib ushlab turilgan taqdirda, bu haqda ushlab turish uchun asos bo‘lgan hujjatlar nusxalari ilova qilingan holda qaysi organ (a) – (b) muddatdan kechiktirmasdan xabar qilinishi shart.",
        "options": [
            "A) (a) – Malaka hay’ati; (b) – uch soatdan;",
            "B) (a) – Sudyalar oliy kengashi; (b) – bir soatdan;",
            "C) (a) – Sudyalar oliy kengashi; (b) – uch soatdan;",
            "D) (a) – Oliy Sud ; (b) – uch soatdan;"
        ],
        "correct": "C) (a) – Sudyalar oliy kengashi; (b) – uch soatdan;"
    },
    {
        "q": "17. Sudyaning turar joyiga kirish, tintuv o'tkazish faqat sud qarori yoki O'zbekiston Respublikasi (a) ruxsati bilan amalga oshiriladi. Sudyaga nisbatan jinoyat ishi O'zbekiston Respublikasi (b) sudloviga tegishlidir.\n1) Bosh prokuror; 2) Sudyalar oliy kengashi; 3) Malaka hay’ati; 4) Oliy sudi;",
        "options": ["A) (a) – 1; (b) – 3;", "B) (a) – 2; (b) – 3;", "C) (a) – 1; (b) – 4;", "D) (a) – 2; (b) – 4;"],
        "correct": "C) (a) – 1; (b) – 4;"
    },
    {
        "q": "18. Sudyaning vakolatlarini qayta tiklash to‘g‘risidagi qaror sudyaning vakolatlarini to‘xtatib turgan tegishli qaysi organ tomonidan qabul qilinadi.",
        "options": [
            "A) Sudyalar malaka hay’ati;",
            "B) Oliy sudi huzurida maslahat organi;",
            "C) Oliy Majlis huzuridagi departament;",
            "D) Qo‘riqlash va avtotransport vazirligi;"
        ],
        "correct": "A) Sudyalar malaka hay’ati;"
    },
    {
        "q": "19. Tumanlararo ma’muriy a’zolari to’g’ri berilgan javobni aniqlang.\n1) sud raisi; 2) sudyalar palatasi kotibi; 3) sudyalar komissiyasi; 4) sudya;",
        "options": ["A) 1,3;", "B) 2,3;", "C) 1,4;", "D) 2,4;"],
        "correct": "C) 1,4;"
    },
    {
        "q": "20. Tumanlararo ma’muriy sud tarkibi ........ sudyadan ortiq bo‘lgan tumanlararo ma’muriy sudda rais o‘rinbosari lavozimi joriy etiladi.",
        "options": ["A) to’rt nafar;", "B) besh nafar;", "C) sakkiz nafar;", "D) olti nafar;"],
        "correct": "D) olti nafar;"
    },
    {
        "q": "21. Quyida berilgan qanday shaxslar O‘zbekiston Respublikasi fuqarosi xalq maslahatchisi bo‘lishi mumkin EMAS.\n1) O‘ttiz besh yoshdan kichik bo‘lmagan;\n2) Yetti yillik yuridik stajga ega bo’lgan shaxslar;\n3) sudya lavozimida ikki yil ishlagan;\n4) yig‘ilishda ochiq ovoz berish yo‘li bilan ikki yarim yil muddatga saylangan;",
        "options": ["A) 1,3;", "B) 2,3;", "C) 1,4;", "D) 2,4;"],
        "correct": "B) 2,3;"
    },
    {
        "q": "22. Quyida berilgan qaysilar Xalq maslahatchilariga oid EMAS.",
        "options": [
            "A) Harbiy xizmatni o‘tayotgan, 35 yoshga to‘lgan... fuqaro harbiy sudning xalq maslahatchisi bo‘lishi mumkin.",
            "B) Har bir sud uchun xalq maslahatchilari soni sudyalarning tegishli sudyalar palatasi tomonidan belgilanadi.",
            "C) Xalq maslahatchilari odil sudlovni amalga oshirishda sudyaning huquqlaridan foydalanadi.",
            "D) Xalq maslahatchilari sudlardagi vazifalarini bajarishga bir yilda ko‘pi bilan ikki haftaga chaqiriladi."
        ],
        "correct": "B) Har bir sud uchun xalq maslahatchilari soni sudyalarning tegishli sudyalar palatasi tomonidan belgilanadi."
    },
    {
        "q": "23. To’g’ri ma’lumot berilgan qatorni aniqlang.\n1) Sudyalarning shaxsiy xavfsizligini ta’minlash maqsadida... xizmat quroli hamda shaxsiy himoya vositalari beriladi.\n2) Zarur hollarda... maxsus davlat xizmati xavfsizligi qurolli soqchilar ajratadi.\n3) Sudyaga nisbatan jinoyat ishi faqat Bosh prokuror tomonidan qo‘zg‘atiladi.\n4) Sudya Senat roziligisiz jinoiy javobgarlikka tortilishi mumkin emas.\n5) Sudyalar daxlsizligini buzganlik taqdimnomasi prokuratura organlari tomonidan bir oy muddatda ko‘rib chiqiladi.\n6) Bosh prokuratura jinoyat ishi qo'zg'atilgani haqida Sudyalar oliy kengashiga xabar beradi.\n7) Sudyani guvoh sifatida so‘roq qilishga tegishli malaka hay’ati roziligi bilan yo‘l qo‘yiladi.",
        "options": ["A) 1,3,5,6,7;", "B) 1,3,5,7;", "C) 2,3,5,6;", "D) 2,4,5,6,7;"],
        "correct": "A) 1,3,5,6,7;"
    },
    {
        "q": "24. Sudyaga nisbatan qamoqqa olish tarzidagi ehtiyot chorasi faqat unga nisbatan qaysi hollarda qo‘llanilishi mumkin.\n1) og‘ir yoki o‘ta og‘ir jinoyat sodir etganlikda;\n2) sudyaning daxlsizligi davrida majlislarda;\n3) odil sudlovni amalga oshirishdagi tartib o’zgargan hollarda;\n4) odam o‘limiga sabab bo‘lgan qasddan boshqa jinoyat sodir etganlikda ayb qo‘yilganda;",
        "options": ["A) 1,3;", "B) 2,3;", "C) 1,4;", "D) 2,4;"],
        "correct": "C) 1,4;"
    },
    {
        "q": "25. Nuqtalar o'rniga mos javobni qo'ying:\na) Sudya ushlangan taqdirda Sudyalar oliy kengashiga u ushlangan paytdan e’tiboran ...... kechiktirmasdan xabar qilinishi shart.\nb) Tintuv o'tkazish faqat sud qarori yoki O‘zbekiston Respublikasi ...... ruxsati bilan amalga oshiriladi.\nc) Sudyaga nisbatan jinoyat ishi O‘zbekiston Respublikasi ...... sudloviga tegishlidir.",
        "options": [
            "A) (a) – qirq sakkiz soat ; (b) – Bosh prokuror; (c) – Oliy sudi;",
            "B) (a) – uch soat; (b) – Bosh vazir ; (c) – Oliy sudi;",
            "C) (a) – uch soat; (b) – Bosh prokuror; (c) – Konstitutsiyaviy sud;",
            "D) (a) – uch soat; (b) – Bosh prokuror; (c) – Oliy sudi;"
        ],
        "correct": "D) (a) – uch soat; (b) – Bosh prokuror; (c) – Oliy sudi;"
    },
    {
        "q": "26. Quyida berilgan qaysi qatorda mantiqiy moslik berilgan?\n1) 15 yillik stajga (kamida 7 yil sudya) -> O'zbekiston Respublikasi Oliy sudi sudyasi\n2) 10 yillik stajga (kamida 2 yil sudya) -> tumanlararo, tuman sudyasi\n3) 35 yosh va 7 yillik staj -> Viloyat, Harbiy sud sudyasi\n4) Ilk bor tayinlanadiganlar -> Sudyalar oliy maktabida majburiy o'qiydi",
        "options": ["A) 1,3;", "B) 2,3;", "C) 1,4;", "D) 2,4;"],
        "correct": "C) 1,4;"
    },
    {
        "q": "27. Lavozimga tayinlanish bo'yicha mantiqiy moslikni toping:\n1) Viloyat sudi raisi -> Prezident tomonidan tayinlanadi\n2) Qoraqalpog'iston sudi raisi -> Jo'qorg'i Kengesh tomonidan tayinlanadi\n3) Qoraqalpog'iston tuman sudi raisi -> Jo'qorg'i Kengesi tomonidan saylanadi\n4) Tuman sudi raisi -> Sudyalar oliy kengashi tomonidan tayinlanadi",
        "options": ["A) 1,3;", "B) 2,3;", "C) 1,4;", "D) 2,4;"],
        "correct": "D) 2,4;"
    },
    {
        "q": "28. XATO ma’lumot berilgan qatorni aniqlang.",
        "options": [
            "A) Davlat organlari va fuqarolar sudyalarni hurmat qilishi va mustaqilligi prinsipiga rioya etishi shart.",
            "B) Sudyaga hurmatsizlik qilish qonunga muvofiq javobgarlikka sabab bo‘ladi.",
            "C) Muayyan ishni ko'rib chiqishga to'sqinlik qilish maqsadida sudyalarga ta'sir ko'rsatish faqat sudyalar ma'muriy javobgarlikka sabab bo'ladi.",
            "D) Sudyadan ko‘rilgan ishlar mohiyati bo‘yicha tushuntirishlar berishni talab qilish taqiqlanadi."
        ],
        "correct": "C) Muayyan ishni ko'rib chiqishga to'sqinlik qilish maqsadida sudyalarga ta'sir ko'rsatish faqat sudyalar ma'muriy javobgarlikka sabab bo'ladi."
    },
    {
        "q": "29. Quyida berilgan qanday shaxslarga sudyalik lavozimiga nomzod bo‘lishi mumkin emas.",
        "options": [
            "A) O‘ttiz besh yoshga to‘lgan;",
            "B) oliy yuridik ma’lumotga ega bo‘lgan;",
            "C) O‘zbekiston Respublikasi fuqarosi;",
            "D) 5 yil muddat O’zbekiston Respublikasi hududida muqim yashagan bo’lishi kerak;"
        ],
        "correct": "D) 5 yil muddat O’zbekiston Respublikasi hududida muqim yashagan bo’lishi kerak;"
    },
    {
        "q": "30. Sudyalarni saylash va tayinlash tartibini o’zaro muvofiqlashtiring:\n1) O‘zbekiston Respublikasi Oliy sudi sudyasi;\n2) Viloyat, tuman, shahar sudi sudyasi;\n3) Qoraqalpog‘iston Respublikasi sudyalari;\n4) Sudyani lavozimga tayinlash tegishli sudyalar.\na) Qoraqalpog‘iston Jo‘qorg‘i Kengesi tomonidan tayinlanadi.\nb) Senat tomonidan saylanadi.\nc) Sudyalar oliy kengashi tomonidan tayinlanadi.\nd) malaka hay’atining xulosasi inobatga olinadi.",
        "options": [
            "A) 1-b; 2-c; 3-a; 4-d;",
            "B) 1-b; 2-c; 3-b; 4-d;",
            "C) 1-b; 2-a; 3-c; 4-d;",
            "D) 1-a; 2-c; 3-b; 4-d;"
        ],
        "correct": "A) 1-b; 2-c; 3-a; 4-d;"
    }
]

# --- SHAKL VA INTERFEYS ---
st.title("⚖️ Sudlar to'g'risida Qonun bo'yicha Test")
st.write("Iltimos, shaxsiy ma'lumotlaringizni to'ldiring va barcha savollarga javob bering.")

st.subheader("📋 Shaxsiy ma'lumotlar")
col1, col2, col3 = st.columns(3)
with col1:
    last_name = st.text_input("Familiya", placeholder="Masalan: Aliyev")
with col2:
    first_name = st.text_input("Ism", placeholder="Masalan: Ali")
with col3:
    middle_name = st.text_input("Otasining ismi", placeholder="Masalan: Vali o'g'li")

st.markdown("---")
st.subheader("❓ Test savollari (30 ta)")

user_selected_answers = {}

for idx, item in enumerate(QUESTIONS, 1):
    st.markdown(f"**{item['q']}**")
    selected = st.radio(
        f"Javobni tanlang ({idx}-savol):",
        options=item["options"],
        key=f"q_{idx}",
        index=None
    )
    user_selected_answers[idx] = selected
    st.write("")

if st.button("📝 Testni tekshirish", type="primary", use_container_width=True):
    if not first_name.strip() or not last_name.strip():
        st.error("⚠️ Iltimos, ismingiz va familiyangizni to'liq kiriting!")
    elif None in user_selected_answers.values():
        st.warning("⚠️ Barcha savollarga javob berishingiz shart! Ba'zi savollar belgilanmagan.")
    else:
        # Natijani hisoblash
        correct_count = 0
        answers_list_for_tg = []
        
        for idx, item in enumerate(QUESTIONS, 1):
            user_ans = user_selected_answers[idx]
            answers_list_for_tg.append(f"Q{idx}: {user_ans}")
            if user_ans == item["correct"]:
                correct_count += 1
                
        total_q = len(QUESTIONS)
        percentage = (correct_count / total_q) * 100
        full_name = f"{last_name.strip()} {first_name.strip()} {middle_name.strip()}".strip()
        
        # Telegramga yuborish
        success, error_msg = send_telegram_notification(
            full_name=full_name,
            score=correct_count,
            total=total_q,
            percentage=percentage,
            user_answers=answers_list_for_tg
        )
        
        if success:
            st.success("✅ Test muvaffaqiyatli topshirildi va Telegram botga yuborildi!")
            st.balloons()
        else:
            st.error(f"❌ Natija hisoblandi, lekin Telegram'ga yuborishda xatolik bo'ldi: {error_msg}")
        
        # Talabaga ko'rinadigan natija
        st.info(f"👤 **Talaba:** {full_name}\n\n"
                f"🎯 **Sizning natijangiz:** {correct_count} / {total_q} ta to'g'ri\n\n"
                f"📊 **Ko'rsatkich:** {percentage:.1f}%")
