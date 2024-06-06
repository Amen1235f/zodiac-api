from flask import Flask,jsonify;
from datetime import datetime;
import random;
app=Flask(__name__)
lucky_descriptions = {
    "Aries": [
        "Today is a great day for new beginnings.",
        "Your energy levels are high; use them wisely.",
        "A surprise is waiting for you around the corner.",
        "Take bold steps towards your goals today.",
        "An exciting opportunity will present itself.",
        "Your confidence will attract positive attention.",
        "A challenge will bring out the best in you.",
        "Someone will appreciate your leadership today.",
        "Your adventurous spirit will lead to a new discovery.",
        "Stay focused on your objectives and you will succeed."
    ],
    "Taurus": [
        "Patience will bring you rewards today.",
        "Take time to enjoy the little things.",
        "A financial opportunity may arise.",
        "Stability and comfort are your allies today.",
        "Trust your instincts in financial matters.",
        "A calm approach will yield the best results.",
        "Someone close to you needs your support.",
        "Your persistence will pay off in unexpected ways.",
        "Take a break and indulge in your favorite activity.",
        "You will find joy in helping others today."
    ],
    "Gemini": [
        "A surprising opportunity will come your way.",
        "Communication is key today.",
        "You will find joy in a new hobby.",
        "Adaptability will be your strength today.",
        "A conversation with a friend brings new insights.",
        "Your curiosity will lead to an interesting discovery.",
        "Today is a good day to start learning something new.",
        "Your quick thinking will solve a problem.",
        "Networking will bring valuable connections.",
        "Express your ideas confidently."
    ],
    "Cancer": [
        "Embrace your emotions today.",
        "Family time will bring you peace.",
        "A creative project will flourish.",
        "Nurture your personal relationships.",
        "Trust your intuition in making decisions.",
        "A heartfelt conversation will bring clarity.",
        "Your nurturing side will be appreciated.",
        "Spend time in a comforting environment.",
        "Your empathy will help someone in need.",
        "A new perspective on an old issue will emerge."
    ],
    "Leo": [
        "Your charisma will attract positive attention.",
        "Take the lead in a group activity.",
        "Express your creativity boldly.",
        "A recognition for your efforts is on the horizon.",
        "Confidence will open new doors for you.",
        "A fun social event is in your future.",
        "Someone will look up to you for guidance.",
        "Your enthusiasm will inspire others.",
        "A leadership opportunity will arise.",
        "Embrace your playful side today."
    ],
    "Virgo": [
        "Attention to detail will be rewarded.",
        "Organize your thoughts and plans.",
        "Helping others will bring satisfaction.",
        "A practical solution to a problem will emerge.",
        "Your analytical skills will be appreciated.",
        "A new project will benefit from your precision.",
        "Take time to declutter your space.",
        "A logical approach will solve a complex issue.",
        "Your advice will be sought after today.",
        "Focus on self-care and well-being."
    ],
    "Libra": [
        "Seek balance in your daily activities.",
        "A harmonious interaction will brighten your day.",
        "Collaboration leads to success.",
        "Focus on maintaining peace in relationships.",
        "Your sense of fairness will be valued.",
        "A social gathering will bring joy.",
        "Your diplomacy will resolve a conflict.",
        "Artistic pursuits will be fulfilling.",
        "A new partnership will be beneficial.",
        "Find time to enjoy beauty around you."
    ],
    "Scorpio": [
        "A deep conversation will be enlightening.",
        "Your determination will lead to success.",
        "An intense focus will help you achieve your goals.",
        "Embrace transformation and change.",
        "A hidden talent will be discovered.",
        "Your passion will drive you forward.",
        "A mystery will unfold in your favor.",
        "Someone will admire your intensity.",
        "Trust your instincts in a challenging situation.",
        "A significant transformation is on the horizon."
    ],
    "Sagittarius": [
        "Adventure is on the horizon.",
        "Learning something new will be rewarding.",
        "Your optimism will inspire others.",
        "A travel opportunity may arise.",
        "Freedom to explore will bring joy.",
        "Your curiosity will lead to an exciting discovery.",
        "A philosophical discussion will be enlightening.",
        "Embrace new experiences with an open heart.",
        "Your enthusiasm will attract positive experiences.",
        "A spontaneous decision will lead to fun."
    ],
    "Capricorn": [
        "Discipline will help you achieve your goals.",
        "Your hard work will be recognized.",
        "A long-term plan will start to take shape.",
        "Practical decisions will lead to success.",
        "Leadership opportunities will present themselves.",
        "Your perseverance will pay off.",
        "Focus on building a solid foundation.",
        "A career advancement is possible.",
        "Your determination will be inspiring.",
        "Take time to reflect on your achievements."
    ],
    "Aquarius": [
        "Innovation will be your key strength today.",
        "Connect with like-minded individuals.",
        "Your unique perspective will be appreciated.",
        "A new idea will gain traction.",
        "Embrace your individuality.",
        "A technological breakthrough is in sight.",
        "Your vision will inspire others.",
        "A group project will benefit from your input.",
        "An unexpected event will lead to a positive outcome.",
        "Think outside the box for a creative solution."
    ],
    "Pisces": [
        "Creativity will flow effortlessly.",
        "A dream or intuition will guide you.",
        "Helping someone in need will bring fulfillment.",
        "Your compassion will be your strength.",
        "A peaceful moment of reflection will be beneficial.",
        "Artistic endeavors will be rewarding.",
        "Your empathy will touch someone's heart.",
        "Spiritual practices will bring peace.",
        "A daydream will inspire a new idea.",
        "Trust your inner voice today."
    ]
}
def get_lucky_description(sign):
    return random.choice(lucky_descriptions.get(sign, ["no description available"]))

@app.route('/zodiac/<sign>/daily', methods=['GET'])
def get_daily_description(sign):
    sign = sign.capitalize()
    description = get_lucky_description(sign)
    if description == "no description available":
        return jsonify({"error": "Invalid zodiac sign"}), 404
    return jsonify({
        "sign": sign,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "lucky-description": description
    })

if __name__ == '__main__':
    app.run(debug=True)