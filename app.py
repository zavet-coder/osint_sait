from flask import Flask, render_template, request, flash, redirect, url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'iouhh-def-secret-key'

@app.context_processor
def inject_year():
    return {'current_year': datetime.now().year}

@app.template_filter('int')
def int_filter(value):
    try:
        return int(float(value))
    except:
        return 0

# Главная
@app.route('/')
def index():
    return render_template('index.html', active_page='home')

# Услуги
@app.route('/services')
def services():
    services_data = [
        {
            'id': 'def_free',
            'title': 'Д3Ф (ПЕРВЫЙ РАЗ)',
            'subtitle': 'Бесплатно для новых клиентов',
            'description': 'Первая защита от преследования абсолютно бесплатно.',
            'icon': '🛡️',
            'price': '0',
            'features': [
                'ПОЛНЫЙ Д0КС ОБИДЧИКА',
                'Д0Н0С НА РАБОТУ/УЧЕБУ',
                'Д0Н0С РОДСТВЕННИКАМ',
                'ПСИХОЛОГИЧЕСКОЕ ДАВЛЕНИЕ',
                'ГАРАНТИЯ РЕЗУЛЬТАТА'
            ]
        },
        {
            'id': 'def',
            'title': 'Д3Ф',
            'subtitle': 'Защита от преследования',
            'icon': '🛡️',
            'price': '10',
            'features': [
                'ПОЛНЫЙ Д0КС ОБИДЧИКА',
                'Д0Н0С НА РАБОТУ/УЧЕБУ',
                'Д0Н0С РОДСТВЕННИКАМ',
                'ПСИХОЛОГИЧЕСКОЕ ДАВЛЕНИЕ',
                'ГАРАНТИЯ РЕЗУЛЬТАТА',
                '🔥 ЗАЩИТА НАВСЕГДА'
            ]
        },
        {
            'id': 'dox',
            'title': 'Д3АН0Н',
            'subtitle': 'Базовый поиск',
            'description': 'Поиск основной информации о цели: телефон, адрес, соцсети, родственники.',
            'icon': '🔍',
            'price': '3',
            'features': [
                'НОМЕР ТЕЛЕФОНА',
                'АДРЕС ПРОЖИВАНИЯ',
                'СОЦСЕТИ (VK, TG, INST)',
                'ФИО',
                'РОДСТВЕННИКИ'
            ]
        },
        {
            'id': 'dox_detailed',
            'title': 'Д3АН0Н+',
            'subtitle': 'Подробный + цепочка',
            'description': 'Максимальная информация + полная цепочка связей и окружение.',
            'icon': '🔎',
            'price': '5',
            'features': [
                'ВСЁ ИЗ БАЗОВОГО',
                'РОДНЯ ДО 3 КОЛЕНА',
                'ДРУЗЬЯ',
                'КОЛЛЕГИ ПО РАБОТЕ',
                'ЦЕПОЧКА СВЯЗЕЙ',
                'СКРЫТЫЕ АККАУНТЫ'
            ],
            'note': 'Информация о друзьях и коллегах предоставляется при наличии в базах'
        },
        {
            'id': 'donos',
            'title': 'Д0Н0С',
            'subtitle': 'Информационная атака',
            'description': 'Доносим ложную информацию родственникам и коллегам обидчика.',
            'icon': '📢',
            'price': '7',
            'features': [
                'Д0Н0С РОДСТВЕННИКАМ',
                'Д0Н0С КОЛЛЕГАМ ПО РАБОТЕ',
                'Д0Н0С НА УЧЕБУ',
                'КОМПРОМЕТИРУЮЩАЯ ИНФОРМАЦИЯ',
                'ПОЛНАЯ АНОНИМНОСТЬ'
            ]
        },
        {
            'id': 'swat',
            'title': 'СВ1ТТИНГ',
            'subtitle': 'Ложное минирование',
            'description': 'Ложное минирование и вызов спецслужб по любому адресу.',
            'icon': '💣',
            'price': '20',
            'features': [
                'МИНИРОВАНИЕ (ШКОЛЫ, ТЦ)',
                'ВЫЗОВ СПЕЦСЛУЖБ',
                '100% АНОНИМНОСТЬ',
                'БЫСТРО (5-10ч)'
            ]
        }
    ]
    return render_template('services.html', services=services_data, active_page='services')

# Оплата
@app.route('/payment/<service_id>')
def payment(service_id):
    services = {
        'def_free': {'title': 'Д3Ф (Первый раз)', 'price': '0'},
        'def': {'title': 'Д3Ф', 'price': '10'},
        'dox': {'title': 'Д3АН0Н', 'price': '3'},
        'dox_detailed': {'title': 'Д3АН0Н+', 'price': '5'},
        'donos': {'title': 'Д0Н0С', 'price': '7'},
        'swat': {'title': 'СВ1ТТИНГ', 'price': '20'}
    }
    service = services.get(service_id, services['def'])
    return render_template('payment.html', service=service, active_page='payment')

# FAQ
@app.route('/faq')
def faq():
    faqs = [
        {'q': '❓ КАК ОПЛАТИТЬ?', 'a': 'Крипта (USDT TRC20) или DonationAlerts. После оплаты пиши @Iouhh_def'},
        {'q': '❓ СКОЛЬКО ЖДАТЬ?', 'a': 'Обычно 5-30 минут. В сложных случаях до 24 часов.'},
        {'q': '❓ ЭТО АНОНИМНО?', 'a': 'Да. Мы не храним логи и не передаем данные.'},
        {'q': '❓ ЕСТЬ БЕСПЛАТНО?', 'a': 'Да. Первый Д3Ф бесплатно для новых клиентов.'},
        {'q': '❓ ВОЗВРАТ?', 'a': '✅ 100% возврат в случае невыполнения услуги. Мы гарантируем результат или вернем деньги.'}
    ]
    return render_template('faq.html', faqs=faqs, active_page='faq')

# Контакты - ТОЛЬКО ТЕЛЕГРАМ
@app.route('/contact')
def contact():
    return render_template('contact.html', active_page='contact')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)