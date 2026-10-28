#!/usr/bin/env python3
"""Generate the DIGIASIA 2026 notes site (single HTML, hash-routed views)."""
import html, json, pathlib, base64

E = html.escape
HERE = pathlib.Path(__file__).parent

# ---------- schedule ----------
SCHEDULE = {
    "1028": ("10/28", "WED", [
        ("10:30–11:00", "Co-Creating the Extraordinary AI for Growth：Creativity, Humanity, and AI", "林友琴、佐佐木康晴（電通）", ["n1028-01", "n1028-01b"]),
        ("14:00–14:20", "Connect the Next：以 AI 驅動新未來", "王俞蓉（LINE）", ["n1028-02"]),
        ("14:20–14:40", "Algorithm of the Heart", "Bharat Avalani", ["n1028-03"]),
        ("14:40–15:00", "Welcome to the Reputation Age", "Fredrik Borestrom（IAA）", ["n1028-04"]),
        ("15:00–15:20", "From Artificial Intelligence to Heartificial Intelligence", "Linda D. Hollebeek", ["n1028-05"]),
        ("15:35–15:55", "AI as the partner, opponent, inevitability and hype", "Sergey Efimov（OMD）", ["n1028-06"]),
        ("15:55–16:15", "當 AI Agent 遇上大數據：OpView Agent Tools", "楊立偉（意藍資訊）", None),
        ("16:15–16:35", "AI 時代下，數位媒體生態系的重構", "夏浩文（艾普特媒體）", None),
        ("16:35–16:55", "Mentor：一站式 AI 廣告投放平台", "藍信彰（台北數位集團）", None),
        ("16:55–17:15", "Why 180 million people don't fit in one prompt", "Muhammad Nafeezul Bari", None),
        ("17:15–18:00", "焦點討論(I)：AI 文藝復興", "主持：陳文琪（佳格）", None),
    ]),
    "1029": ("10/29", "THU", [
        ("10:00–10:30", "Beyond Automation：Human-Centered AI for the Future of Marketing", "宮部裕介（博報堂）", None),
        ("10:30–11:00", "沒有 AI，靈魂放不大", "Sulin Lau（Grab）", None),
        ("11:00–11:30", "Becoming Frontier：Agentic AI Transformation", "Mahesh Neelakantan（Microsoft）", None),
        ("11:30–12:00", "AI 時代的挑戰：建構詐騙聯防網，重建數位信任", "主持：盧諭緯", None),
        ("14:00–14:30", "焦點討論(II)：AI 時代中小型廣告行銷業者的突破之道", "主持：王冠翔", None),
        ("14:30–14:50", "代理商的行銷 AI 轉型", "張志浩（麥肯）", None),
        ("14:50–15:10", "Precise Targeting with Geofencing", "Jay Kim（AAAZA）", None),
        ("15:10–15:30", "用 AI 引領，每天更懂你", "蔣仲閔（Yahoo）", None),
        ("15:45–16:05", "The Right Thing at the Right Moment", "Sam Lam（Roctec）", None),
        ("16:05–16:25", "YouTube Partner Sales 與 Criteo Commerce Data", "虞秉儒、張景翔", None),
        ("16:25–16:45", "臺灣文化科技的新命題", "劉俊裕（臺藝大）", None),
        ("16:45–17:05", "AI 能加速產量，但打動人心的仍是人的判斷", "湯昇榮（瀚草）", None),
        ("17:05–17:25", "當想像「即時上映」", "林家齊（夢想動畫）", None),
    ]),
}

# ---------- notes ----------
# block types: ("p", [lines]) ("table", head, rows) ("ol", items) ("ul", items) ("quote", [lines]) ("flow", items, hi) ("aside", [lines])
NOTES = [
    {
        "id": "n1028-01", "bio": ['台灣人，奧美出身。', '1999 年創立數位代理商「知世網絡」，後加入安索帕（Isobar），升任全球執行長。', '電通併購安索帕後，2023 年升任電通集團全球專業服務總裁。'], "bio_src": '數位時代', "day": "10/28 WED", "time": "10:30–11:00",
        "title": "Co-Creating the Extraordinary AI for Growth",
        "speaker": "林友琴", "role": "電通集團 全球品牌長",
        "kicker": "開場引言，主講為佐佐木康晴（另一份筆記）",
        "index": [("把心放進去", "硬體已經到位，缺的是人心"), ("創新帶來影響", "電通 125 年的核心信念"),
                  ("B2B2S", "成果要延伸到社會"), ("3A", "受眾、演算法、AI 代理"), ("AI 驅動成長", "不只追求效率")],
        "summary": [
            ("台灣的下一步", ["全球 90% 的 AI 伺服器，由台灣企業製造。", "硬體已經到位。", "真正的問題是：怎麼把人心放進去？"]),
            ("創新，要以影響力為目標", ["電通今年 125 週年，信念是「創新帶來影響」。", "AI 讓環境變得更複雜，所以必須創新。", "但創新不能只是新，還要帶來影響。"]),
            ("影響力不只是生意", ["電通自稱 B2B2S 公司，也就是「企業對企業對社會」。", "和客戶、夥伴一起合作，成果才能延伸到社會。", "講者認為，這正是廣告產業不會被 AI 取代的原因。"]),
            ("品牌要贏三場仗", ["受眾、演算法、AI 代理。"]),
            ("AI 是為了成長", ["AI 不該只拿來省時間。", "它要創造新價值，打開新市場。"]),
        ],
        "frameworks": [
            ("品牌成長的 3A", [("table", ["A", "意思"], [["贏得受眾", "讓人選擇你"], ["贏得演算法", "讓平台推薦你"], ["贏得AI 代理", "讓 AI 代理選擇你"]]),
                             ("aside", ["講者只列出 3A，沒有逐項說明。「意思」一欄依字面整理。"])]),
            ("創新帶來影響的三個面向", [("table", ["面向", "說明"], [["AI 驅動成長", "創造新價值，不只做優化"], ["系統性創新", "讓價值隨時間累積"], ["敏捷整合", "圍繞客戶核心，交出實際成果"]]), ("img", "6168", "Innovating to Impact 三個面向")]),
        ],
        "quotes": [["影響力，是成功運用 AI 最關鍵的要素。"]],
        "cases": [
            ("電通台灣 1,200 人合照", [("p", ["講者用這張照片，說明台灣的特質：", "文化豐富，人情溫暖。"])]),
            ("DIGIASIA 來到台北", [("p", ["講者當年參與團隊，爭取大會在台北舉辦。", "她認為，DIGIASIA 和電通的理念一致：", "讓亞洲在全球發出更大的聲音。"])]),
        ],
        "actions": [
            ("媒體企劃", [["用 3A 檢視現有的媒體計畫。", "預算是不是只放在「受眾」？", "有沒有經營平台演算法？", "AI 搜尋、購物助理裡，品牌有沒有出現？"],
                         ["提案時，寫 AI 帶來的成長。", "不要只寫省了多少時間。"]]),
            ("客戶服務", [["回報成效時，除了生意數字，", "也說明品牌和社會層面的影響。"]]),
        ],
    },
    {
        "id": "n1028-01b", "bio": ['1995 年以文案身分進入電通，大學念資訊工程，是互動廣告的先驅。', '2014 年創立 Dentsu Lab Tokyo，2023 年起任電通全球創意長。', '2025 年被 Campaign Brief Asia 評為亞洲得獎最多的創意領袖，擔任過坎城、Clio、ADFEST 等國際廣告獎評審主席。'], "bio_src": 'dentsu 官網、林友琴引言', "day": "10/28 WED", "time": "10:30–11:00",
        "title": "AI for Growth: Creativity, Humanity, and AI",
        "speaker": "佐佐木康晴 Yasu Sasaki", "role": "dentsu 全球創意長",
        "kicker": "與林友琴同場次",
        "index": [("AI 驅動成長", "AI 實驗期已過，要拿來做出成果"), ("PSDCA", "在 PDCA 裡加入「模擬」"),
                  ("創作者在迴圈中", "AI 進入流程，人的創意留在核心"), ("留白", "人做得到、AI 做不到的事"),
                  ("Heartificial", "用 AI 省下的時間，做有溫度的作品")],
        "summary": [
            ("用不用 AI，已經不是問題", ["去年講者問台下：「誰在用 AI？」", "今年，這個問題已經過時了。", "現在每家企業都在想：怎麼用 AI 做出成果？"]),
            ("電通的 AI 策略，有三個要素", ["模擬、整合、人的洞察 × AI。"]),
            ("AI 廣告越來越像", ["市面上 AI 做的廣告越來越多，", "看起來卻都似曾相識。", "差異，要靠人做出來。"]),
            ("AI 不只拿來做影片、投廣告", ["電通的創意團隊，把 AI 用在照護、兒童閱讀、地方媒體。", "創意人的新任務，是想出 AI 的新用法。"]),
            ("人的角色：打破 AI 的完美答案", ["AI 能同時給出很多完美答案。", "人要做的，是把它打破，讓它更有趣、更新、更強。"]),
        ],
        "frameworks": [
            ("電通 AI 策略三要素", [("table", ["要素", "說明"], [["模擬", "用 AI 試跑各種可能，選出最有機會的一個"], ["整合", "不給零散工具，給一整套環境"], ["PI × AI", "人的洞察（People Intelligence）結合 AI，做出差異"]])]),
            ("PSDCA", [("flow", ["計畫", "模擬", "執行", "檢查", "行動"], 1),
                       ("p", ["模擬怎麼做？"]),
                       ("ol", ["用 AI 產出大量選項。", "用虛擬人物訪談、AI 市場檢查，反覆測試。", "選出最有可能成功的方案，再提案。"]), ("img", "6170", "PSDCA 模型")]),
            ("AI for Growth Suite", [("p", ["日本已有數十家客戶導入。"]),
                                     ("table", ["工具", "功能"], [["People Research", "虛擬量化調查"], ["Talk", "虛擬人物深度訪談"], ["Flash", "點子發想"], ["Plot", "策略規劃"], ["Canvas", "AI 代理平台"]]),
                                     ("p", ["每個工具，都內建電通專家的知識。", "共有 10 種專業 AI 代理，可以當成團隊成員。"]), ("img", "6176", "AI for Growth Suite 工具總覽")]),
            ("創作者在迴圈中（Creator-in-the-loop）", [("quote", ["AI 在流程裡。人的創意在核心。差異，靠設計。"]),
                                                     ("table", ["做法", "說明"], [["催化型點子", "點子持續變形，讓人參與、加入、擴散"], ["智慧故事系統", "一個故事，用 AI 調整成適合每個接觸點的版本"]]),
                                                     ("p", ["目的：避開 AI 時代的同質化。"]), ("img", "6177", "Creator-in-the-loop")]),
            ("AI 求完美，人負責打破", [("table", ["AI 擅長", "人擅長"], [["從資料找出模式", "問出「什麼才重要」"], ["提升短期效率", "創造長久的喜愛"], ["同時產出大量版本", "選出最重要的那一個"], ["為每個人個人化", "說一個大家都愛的故事"], ["24 小時不停發想", "提出大膽、負責的點子"], ["自動大量生產", "慢慢做出打動人的工藝"], ["精簡、有效率", "有「浪費」、有留白"]]),
                                    ("p", ["講者特別強調最後一項。", "有留白，人才會好奇、想參與。", "這是 AI 做不到的。"]), ("img", "6185", "AI Perfects. Humans Disrupt.")]),
        ],
        "quotes": [["AI 已經結束實驗階段。"], ["AI 能同時做出很多完美答案。", "人的角色，是把它打破。"], ["從創意人，到 AI 打造者。"], ["用 AI 多出來的時間，", "去做更強、更有差異、更有心的作品。"]],
        "cases": [
            ("電通 2026 CMO 調查", [("p", ["每年調查約 2,000 位 CMO。"]), ("stats", [("79%", "認為光靠 AI，無法成為競爭優勢"), ("78%", "認為和代理商合作的樂趣，是能遇到帶來意外點子的有趣夥伴"), ("80%+", "認為未來差異更重要，而差異來自人的創意")]), ("img", "6178", "Dentsu Creative 2026 CMO Report")]),
            ("三得利 JJ（茉莉花燒酎調酒）", [("ul", ["情境：晚上 23:55，兩人邊喝酒邊聊天。想再多聊一點，但末班車快沒了。", "AI 的分工：整個場景、環境和背景，都由 AI 生成。", "人的分工：只有人物是實際拍攝。", "重點：畫面交給 AI，情感交給人。", "片中台詞：「今天變成明天的五分鐘前，我們的心意來來回回。」"])]),
            ("照護的目光計畫", [("ul", ["背景：2035 年，日本每 3 人就有 1 位高齡者。好的照護靠個人經驗，很難傳承。", "做法：用智慧眼鏡記錄照護現場，再由 AI 解讀。", "成果：首次整理出 14 項心法、30 個動作，變成現場培訓課程。", "重點：把個人的隱性知識，變成大家共享的資產。"]), ("img", "6179", "The Gaze of Care Project")]),
            ("Haptale：摸得到的故事", [("ul", ["背景：孩子因為手機和社群，遠離書本。", "做法：Dentsu Lab 開發能生成「觸覺」的 AI。把 42 個擬聲詞對應到觸感，任何文字都能變成手感。", "例子：野獸的大白骨，粗粗的；蓮花，軟軟的。", "成果：超過 13,000 人體驗。家長說：「平常不看書的孩子，今天完全看入迷。」"]), ("img", "6180", "Haptale 書中物件的觸感")]),
            ("德川家康 AI「SUNPU」", [("ul", ["靜岡新聞社開發。", "AI 學習德川家康的知識，加上靜岡新聞的歷年報導。", "設計成吉祥物，和地方企業家對談地方的未來，連孩子都看得懂。", "重點：地方媒體用 AI，和在地建立新關係。"]), ("img", "6181", "德川家康 AI「SUNPU」")]),
            ("電通 × 東京大學研究（約 4 年）", [("ul", ["研究一：拿掉 AI 的常識框架。", "題目：「想一個新的婚禮形式」。", "一般 AI：環保婚禮。正確，但無聊。", "拿掉框架的 AI：訂閱制婚禮。不辦婚禮，改成每月付費，每月收到夫妻的幸福近況。", "研究二：設計靈感。好點子需要「專注」和「放鬆」的平衡。電通開發了幫助兩者切換的工具，原型已完成。"]), ("img", "6183", "Research 2：Designing Inspiration")]),
        ],
        "actions": [
            ("媒體企劃", [["排期前，多一步「模擬」。", "先用 AI 試跑幾種預算配置和通路組合，再挑一個執行。"],
                         ["前期洞察，可以先用虛擬人物訪談、虛擬調查快速驗證。", "正式決策前，仍要用真實數據確認。"],
                         ["素材規劃用「一個故事、多個版本」。", "先定核心故事，再依各媒體調整形式。"]]),
            ("創意", [["AI 的第一個答案，通常正確但無聊。", "刻意要求 AI 打破常識，再由人挑選。"],
                      ["作品留一點白，讓受眾想接話、想參與。"],
                      ["參考 JJ 的分工：場景交給 AI，演員實拍。", "情感的部分，留給真人。"]]),
            ("客戶服務", [["提案時可以引用 CMO 調查。", "79% 的 CMO 認為，光靠 AI 無法成為競爭優勢。", "代理商的價值，在於意外的點子。"]]),
        ],
    },
    {
        "id": "n1028-02", "bio": ['LINE 台灣企業解決方案事業群總經理。', '這個事業群負責官方帳號、廣告等企業服務。', '公開資料未查到更早的經歷。'], "bio_src": '大會講者頁、旺得富', "day": "10/28 WED", "time": "14:00–14:20",
        "title": "Connect the Next：以 AI 驅動新未來",
        "speaker": "王俞蓉", "role": "台灣連線（LINE）企業解決方案事業群 總經理",
        "kicker": "",
        "index": [("全民觸及", "2,200 萬用戶，觸及率全球之冠"), ("官方帳號", "企業接觸消費者最重要的武器"),
                  ("@AI", "在聊天和群組裡直接叫 AI 幫忙"), ("AI 代理", "每個官方帳號都能有自己的 AI 代理"),
                  ("2027 Q1", "官方帳號 AI 代理平台正式推出")],
        "summary": [
            ("在台灣，LINE 幾乎等於全台灣", ["台灣人口 2,300 萬，LINE 用戶 2,200 萬。", "扣掉還沒有手機的小孩，有手機的人幾乎都裝了 LINE。", "用戶密度和觸及率，是全球之冠。"]),
            ("LINE 早就不只是聊天", ["發展 15 年，延伸出六大服務：", "通訊、社群、企業服務、移動、金融科技、電商與內容。"]),
            ("官方帳號，是企業最重要的武器", ["台灣官方帳號已累積 360 萬個，還在快速成長。", "86% 的用戶有在使用官方帳號。", "使用率最高的是零售電商和餐廳。", "今年還有一個特別現象：下個月選舉，六都候選人都在經營官方帳號。"]),
            ("LINE 的 AI，從三個面向切入", ["人性、意圖、行動。"]),
            ("官方帳號將進入 AI 代理時代", ["每個官方帳號，都能有自己的 AI 代理。", "目前進行品牌驗證，預計 2027 年第一季正式推出。"]),
        ],
        "frameworks": [
            ("LINE 六大服務", [("table", ["面向", "服務"], [["通訊", "LINE 聊天、社群"], ["企業服務", "官方帳號、LINE Mini App、LAP 廣告"], ["移動", "LINE GO（原 LINE TAXI）"], ["金融科技", "LINE Pay、LINE Bank"], ["電商", "LINE 購物、LINE 禮物"], ["內容", "LINE TODAY"]]),
                              ("img", "6194", "LINE 生態系六大服務")]),
            ("Connect the Next：AI 的三個面向", [("table", ["轉變", "在 LINE 裡的樣子"], [["從技術，到人性", "聊天、群組裡直接 @AI 幫忙"], ["從注意力，到意圖", "推出「吃、玩、買」三個 AI 代理，更懂用戶需求"], ["從對話，到行動", "官方帳號的 AI 代理，直接幫顧客完成任務"]]),
                                              ("img", "6199", "Connect the Next 三個面向")]),
            ("官方帳號 AI 代理平台", [("table", ["特色", "說明"], [["三種角色", "預約、銷售、客服"], ["一鍵啟用", "基礎功能（簡單問答、加入行事曆）＋進階功能（會員資料、會員卡、提醒）"], ["開放串接", "已有 SaaS 服務的商家，可以讓第三方夥伴接進來"], ["自由搭配", "大、中、小型品牌都能彈性組合"]]),
                                 ("p", ["在後台用對話，就能完成設定。", "目前到 10 月底進行品牌驗證，預計 2027 年第一季正式推出。"]),
                                 ("img", "6198", "選擇 AI 代理角色，搭配需要的能力")]),
            ("官方帳號的生態系循環", [("flow", ["AI 代理", "對話更輕鬆", "好友黏著度提高", "更了解顧客", "第一方數據分析", "投放 LINE 廣告"], 0),
                                    ("p", ["官方帳號是核心，串起 LINE 所有服務。", "數據分析完，可以打包投放到 LINE 廣告平台，", "形成一個完整的循環。"])]),
        ],
        "quotes": [["讓每一次的對話，", "都更靠近生意的轉換。"]],
        "cases": [
            ("數字看台灣的 LINE", [("stats", [("2,200 萬", "台灣 LINE 用戶（人口 2,300 萬）"), ("360 萬", "台灣官方帳號數"), ("86%", "用戶有在使用官方帳號")]),
                                  ("img", "6196", "官方帳號數成長至 360 萬"),
                                  ("stats", [("20.2 分鐘", "語音通話"), ("23.5 分鐘", "視訊通話"), ("2.6 次", "通話次數")]),
                                  ("aside", ["每人每天平均（發話方），資料來源：LINE 內部數據。"]),
                                  ("img", "6195", "連結你我的每一天")]),
            ("群組裡的 @AI", [("ul", ["分工總結：週末烤肉，群組一直在討論誰帶酒、誰帶肉、誰接送。@AI 說「幫我總結」，就會整理成分工表，放進記事本。", "行事曆：群組約好的聚餐和活動，@AI 直接加進行事曆，時間到了會提醒。", "相簿：出遊照片洗版時，叫 AI 建一個相簿放進去，不用自己一張張設定。"]),
                              ("img", "6197", "解答疑問，幫忙搞定")]),
            ("美甲店預約", [("ul", ["情境：想約常配合的美甲師，但對方那個時段沒空。", "AI 代理：主動推薦另一位有空的美甲師，顧客同意後直接完成預約。", "對顧客：立刻約好，不用等店長回訊息，也不用自己對時間。", "對商家：每一次對話，都更靠近成交。"])]),
        ],
        "actions": [
            ("媒體企劃", [["把 LINE 當成台灣的基礎觸及。", "用戶 2,200 萬，幾乎涵蓋所有有手機的人。"],
                         ["規劃「官方帳號＋廣告」的循環。", "用官方帳號累積好友和第一方數據，", "分群後再投放 LINE 廣告。"],
                         ["KPI 從「好友數」轉向「任務完成」。", "例如預約數、詢問轉成交的比例。"]]),
            ("客戶服務", [["零售電商、餐廳客戶優先溝通。", "這兩類官方帳號使用率最高，", "最適合先導入預約或銷售 AI 代理。"],
                         ["2027 年第一季正式推出前，", "先幫客戶盤點：要用哪一種 AI 代理？", "現有的 SaaS 系統能不能串接？"]]),
            ("數據", [["官方帳號的好友數據是第一方數據。", "AI 代理上線後，對話資料會更完整，", "可以提早規劃分析和分群的方式。"]]),
        ],
    },
    {
        "id": "n1028-03", "bio": ['前聯合利華區域品牌傳播總監，有 25 年品牌管理和媒體策略經驗，工作足跡遍及 69 個國家。', '現為說故事顧問，也是 Anecdote International 全球合夥人。', '曾任 IAA 馬來西亞分會會長，現任亞洲廣告聯盟（AFAA）執行委員。'], "bio_src": 'London Speaker Bureau Asia', "day": "10/28 WED", "time": "14:20–14:40",
        "title": "Algorithm of the Heart",
        "speaker": "Bharat Avalani", "role": "Connecting the Dots Malaysia 創辦人",
        "kicker": "",
        "index": [("心的演算法", "最古老的演算法，就是說故事"), ("知道 vs 相信", "理性讓人知道，故事讓人相信"),
                  ("先連結", "先連結，再計算或修正"), ("故事 DNA", "時間地點、順序、人物、意外、商業重點"),
                  ("故事銀行", "平常就收集自己的故事")],
        "summary": [
            ("文字正在貶值，說話會更有價值", ["講者提到，Google 正在開發偵測 AI 內容並降低排序的演算法。", "LinkedIn 也鼓勵人自己寫，不要交給機器。", "當文字越來越不值錢，口說的話會越來越有價值。"]),
            ("最古老的演算法：心的演算法", ["六萬年前，印尼蘇拉威西的洞穴壁畫，就在分享打獵的經驗。", "台灣的八仙洞，也有約三萬年的歷史。", "講者把這個演算法，稱為「說故事」。"]),
            ("數據帶來共識，故事帶來行動", ["數據、分析、流程，能讓大家達成共識。", "但要讓人行動，必須把它們轉成信念、信任和連結。"]),
            ("商業說故事，是一門科學", ["它有固定的 DNA，也有明確的目的：", "傳達訊息、讓提案通過、推動行動。"]),
            ("不要說「我要講一個故事」", ["在商業場合，這句話會讓人懷疑你的可信度。", "直接分享一個經驗、一個時刻就好。"]),
        ],
        "frameworks": [
            ("理性 vs 故事", [("table", ["", "是什麼語言", "做什麼"], [["理性", "「知道」的語言", "描述發生了什麼"], ["故事", "「相信」的語言", "讓人看見、感受到"]]),
                             ("p", ["只給數字，人不一定相信。", "把數字配上一個親身經歷，數字才會變成信念。"]),
                             ("img", "6200", "Reason is the language of knowing. Story is the language of believing.")]),
            ("讓人行動的三個轉換", [("table", ["從", "轉成"], [["數據", "信念"], ["分析", "信任"], ["流程", "連結"]]),
                                   ("quote", ["機器會計算、會修正。只有人能連結。"])]),
            ("故事的 DNA", [("table", ["元素", "說明"], [["時間與地點", "讓聽眾能在腦中看見畫面"], ["事件順序", "清楚的時間線，讓人跟得上"], ["人物與對話", "一兩個真實人物，加上真實的對話"], ["意外元素", "一個讓人意外的觀點或轉折"], ["商業重點", "不是為了娛樂，是為了傳達訊息、推動行動"]]),
                           ("aside", ["講者示範：「我昨天花了 16 個小時來到台北，提早 5 分鐘降落」是時間；「從喜馬拉雅山區搭車、轉火車、再轉兩班飛機」是地點和順序。"])]),
            ("故事的三個層次", [("table", ["層次", "效果"], [["一個故事", "描述發生了什麼"], ["好故事", "讓你看見發生了什麼"], ["偉大的故事", "讓你感受到發生了什麼"]])]),
            ("建立你的故事銀行", [("p", ["台灣人很會存錢，也請開一個「故事銀行」。", "故事有三種來源："]),
                                 ("ol", ["自己的故事", "別人告訴你的故事", "你讀到的故事"]),
                                 ("p", ["能用自己的故事，就用自己的。", "怎麼找？每天睡前，想想今天讓你開心和難過的時刻。", "故事，就藏在這兩者之間。"])]),
        ],
        "quotes": [["理性是「知道」的語言。", "故事是「相信」的語言。"], ["機器會計算、會修正。", "只有人能連結。"], ["先連結，", "再計算或修正。"]],
        "cases": [
            ("新舊 CEO 的交接大會", [("ul", ["背景：2019 年，香港一家大型顧問公司換 CEO，交接最後一天開全員大會。", "舊 CEO：講電影《關鍵少數》。NASA 主管 Dorothy Vaughan 看到 IBM 電腦進駐，擔心工作被取代，當天就去圖書館自學 Fortran 程式語言，再教會整個團隊。最後他問：「公司在轉型，我們的 Fortran 是什麼？」", "新 CEO：哈佛出身，願景、使命、數字樣樣齊全。講者給他 11 分（滿分 10 分）。", "結果：散會後，幾乎所有人都去找舊 CEO 討論轉型的點子，新 CEO 一個人站在原地。"])]),
            ("雅加達的「快樂混亂」", [("ul", ["數據：雅加達的交通很糟。", "親身經歷：有人要切進來，駕駛會讓路，認為對方可能在趕時間；還有志工幫忙指揮。", "結論：交通很亂，但是一種「快樂的混亂」。", "重點：數據配上親身經歷，就有說服力。"])]),
            ("記憶小測驗", [("p", ["講者用一個記憶小測驗示範：", "跟熟悉的畫面連結，人才記得住。"])]),
        ],
        "actions": [
            ("媒體企劃", [["提案時，數據後面接一個真實片段。", "例如不只說觸及率，再說一個消費者實際接觸到廣告的時刻。"],
                         ["開場不要說「我來講個故事」。", "直接說「上週我們在投放時看到……」。"],
                         ["用故事 DNA 檢查提案：", "有沒有時間地點？順序清不清楚？", "有沒有真實的人和對話？", "有沒有意外的觀點？商業重點是什麼？"]]),
            ("創意", [["講者提到平台開始對 AI 生成的文字降權。", "內容要保留人的觀點和聲音。"]]),
            ("全體", [["建立團隊的故事銀行。", "收集客戶、消費者、投放現場的真實片段，提案時隨時可以用。"]]),
        ],
    },
    {
        "id": "n1028-04", "bio": ['國際廣告協會（IAA）全球會長。', '正職是 LinkedIn 歐洲、中東、非洲與拉丁美洲區的代理商發展負責人。', '曾任職 Euronews、Eurosport 與行動行銷公司，有近 20 年經驗。'], "bio_src": 'IAA 官網、大會講者頁', "day": "10/28 WED", "time": "14:40–15:00",
        "title": "What's Coming Next? Welcome to the Reputation Age",
        "speaker": "Fredrik Borestrom", "role": "IAA 全球會長暨主席｜LinkedIn 全球代理商運營總監",
        "kicker": "以 LinkedIn 身分分享 B2B Buyability 研究",
        "index": [("Buyability", "品牌如何被一群人選中"), ("隱形買家", "握有將近一半的決策權"),
                  ("決策安全感", "B2B 賣的是「選錯也能辯護」"), ("3R", "推薦、關係、共鳴"),
                  ("3 個信號", "創意裡放進 3 個以上，成效大幅提升")],
        "summary": [
            ("B2B 採購，是一群人在決定", ["一個採購小組，平均有 22 到 23 人。", "其中將近一半是「隱形買家」：採購、法務、營運主管。", "行銷長期忽略了他們。"]),
            ("B2B 賣的不是功能，是安全感", ["買杯咖啡，選錯了沒關係。", "選 CRM、資安、金融夥伴，選錯了可能丟工作。", "34% 的人選擇廠商，主因是「出事時能為這個選擇辯護」。"]),
            ("讓整個採購小組都認識你", ["整個小組都認識品牌，被選中的機率最高可達 20 倍。", "只有主要決策者認識，勝率只剩 4%。"]),
            ("成交，靠 3R", ["推薦、關係、共鳴。", "把這三種信號放進溝通裡，才能推動成交。"]),
            ("創意裡放進 3 個以上信號，成效大幅提升", ["分析 700 件坎城 B2B 作品，52% 只用了 0 或 1 個信號。", "用了 3 個以上的作品，回報品牌指標、ROI、營收改善的機率都明顯更高。"]),
        ],
        "frameworks": [
            ("B2B 行銷長期投資不足的三件事", [("table", ["項目", "說明"], [["安撫隱形買家", "他們的工作是「否決風險」，很容易說不"], ["賣決策安全感", "給採購小組「選錯也能辯護」的職涯保障"], ["製造 3R 信號", "推薦、關係、共鳴，才是成交的關鍵"]]),
                                            ("img", "6202", "B2B marketing systematically underinvests in")]),
            ("3R：讓人成交的三種信號", [("table", ["信號", "說明"], [["推薦", "客戶、同業或專家，獨立為品牌背書"], ["共鳴", "買方在產品或案例裡看到自己：同類公司、同樣用途"], ["關係", "買方或其公司和品牌之間，已經累積熟悉度或連結"]]),
                                      ("img", "6204", "The signals that close deals：3Rs")]),
            ("採購小組會問的五個問題", [("ol", ["這家廠商擅長處理像我們這樣的情況嗎？", "我的人脈怎麼看？", "我們或同類公司跟他們合作過嗎？", "同業推薦他們嗎？", "他們的工作風格跟我們合得來嗎？"]),
                                      ("p", ["這五個問題，也是 AI 代理評估廠商時會問的。", "買方會把這些問題直接輸入 ChatGPT、Gemini、Copilot、Claude。", "準備好回答這些問題的內容，品牌才會出現在 AI 推薦的前面。"])]),
            ("信任堆疊（Credibility Stack）", [("table", ["層次", "角色"], [["品牌", "提出觀點和定位"], ["員工", "讓訊息有人味。人比較信任人，品牌信任度正在歷史低點"], ["客戶與擁護者", "外部驗證，讓可信度更穩固"], ["創作者", "擴大聲量。在 B2B 正在興起"]]),
                                             ("p", ["四層要一起運作，信任才會累積。"]),
                                             ("img", "6205", "The Credibility Stack")]),
            ("七個 Buyability 信號", [("ol", ["表明服務過「像你這樣的客戶」", "客戶推薦", "同業或專家推薦", "網紅或名人合作", "表明工作風格相近", "長期合作關係", "品類領導地位"]),
                                    ("p", ["不需要七個全用。30 秒的廣告很難塞滿，", "用到 3 個以上，效果就很明顯。"])]),
        ],
        "quotes": [["在 B2B，", "你賣的是職涯安全感。"], ["能為選擇辯護，", "比規格和 AI 模型更重要。"]],
        "cases": [
            ("數字看 B2B 採購", [("stats", [("22–23 人", "採購小組平均人數"), ("49%", "決策權在隱形買家手上"), ("34%", "因為「出事時能辯護」而選擇廠商")]),
                                ("stats", [("20 倍", "整個小組都認識品牌時，被選中的機率"), ("4%", "只有主要決策者認識品牌時的勝率"), ("40%", "B2B 交易因為有人說「不」而沒成交")]),
                                ("img", "6203", "Hidden Buyers have huge decision rights")]),
            ("700 件坎城 B2B 作品分析", [("ul", ["研究：LinkedIn 和 WARC、Lions Advisory 合作，分析 700 件入圍坎城獅子獎的 B2B 作品。", "發現：平均每件只用了 1.6 個信號，52% 只用了 0 或 1 個。廣告測試公司 System1 也發現，B2B 廣告多半只拿到 0 或 1 顆星（滿分 5 顆）。"]),
                                        ("img", "6206", "Even the best B2B campaigns score mostly zero or one signals"),
                                        ("p", ["用了 3 個以上信號的作品，和其他作品相比："]),
                                        ("stats", [("+91%", "回報中段漏斗指標（考慮度、偏好度、購買意圖）改善的機率"), ("+63%", "回報投資報酬率（ROI）提升的機率"), ("+110%", "回報增量營收成長的機率")]),
                                        ("img", "6207", "Three or more stacked signals deliver amplified impact")]),
            ("ServiceNow", [("ul", ["公司：美國企業軟體公司。用雲端平台串起 IT、人資、客服等部門的工作流程，近年主打 AI 代理。", "觀念：品牌長 Jim Lesser 把 Buyability 當成核心創意系統，不是短期戰術。", "主廣告：2024 年 5 月起推出的系列廣告，由 BBDO 紐約製作。英國演員 Idris Elba 飾演熱情推廣 AI 的 CEO，帶著愛吐槽的助理 Nick 巡視公司，並搭配一群代表不同職能的角色：資安偵探、客服大師、IT 巫師、HR 超級巨星、採購主管、財務經理。不論觀眾在哪個部門，都能看到自己。", "成績：命中 7 個信號中的 4 個。", "延伸廣告：由「IT 巫師」Patty 主演的下層漏斗廣告，不需要大製作。文案像是「一個工作流程，勝過 100 個權宜之計」「讓你的 AI 跑起來，但不要失控」，直接打中 IT 主管（資料來源：現場簡報）。"]),
                            ("img", "6208", "ServiceNow IT 巫師 Patty 系列廣告")]),
        ],
        "actions": [
            ("媒體企劃", [["受眾從「主要決策者」擴大到「整個採購小組」。", "把採購、法務、營運這些隱形買家也納入溝通對象。"],
                         ["KPI 不要只看下層轉換。", "用 3 個以上信號的作品，回報中段漏斗指標改善的機率高出 91%，", "考慮度、偏好度、購買意圖要一起看。"],
                         ["用信任堆疊排發聲管道：", "品牌官方、員工帳號、客戶證言、創作者合作，", "四層一起規劃，不要只投品牌廣告。"],
                         ["為 AI 搜尋準備內容。", "針對採購小組的五個問題，準備案例、客戶推薦、合作年資等內容，", "讓品牌在 AI 推薦裡排得更前面。"]]),
            ("創意", [["用七個信號檢查 B2B 素材，至少放進 3 個。"],
                      ["讓不同職能的人，都能在素材裡看到自己。", "參考 ServiceNow 的角色設計。"]]),
            ("客戶服務", [["和 B2B 客戶溝通時，把「出事時能不能辯護」當成訴求重點，", "不要只講產品功能。"]]),
        ],
    },
    {
        "id": "n1028-05", "bio": ['馬來西亞 Sunway University 行銷講座教授，也在愛沙尼亞、瑞典、南非等地的大學任教。', '2020 年起連年獲選 Clarivate「全球高被引研究者」。', '被視為全球顧客互動（customer engagement）研究的領先學者。'], "bio_src": 'Sunway University 官網', "day": "10/28 WED", "time": "15:00–15:20",
        "title": "From Artificial Intelligence to Heartificial Intelligence",
        "speaker": "Linda D. Hollebeek", "role": "Sunway University 等多所大學 教授",
        "kicker": "用 AI 加深顧客與品牌的互動",
        "index": [("能力 ≠ 互動", "AI 更強，不代表顧客更投入"), ("放大，不取代", "AI 處理例行工作，人專注創意和關係"),
                  ("四種價值", "認知、情感、行為、關係"), ("人的四種能力", "創意、同理、好奇、判斷"),
                  ("效率 vs 意義", "AI 讓顧客走完旅程，意義讓顧客留下")],
        "summary": [
            ("能力更強，不等於互動更深", ["AI 從分析預測，進化到生成內容，再到自主執行。", "但技術再先進，也可能只帶來膚淺的顧客體驗。", "自動化，不保證真正的連結。"]),
            ("顧客和品牌的關係，本質是情感", ["我們和品牌互動，不只是為了效率。", "而是因為它讓我們有感覺、讓我們理解，我們也信任它。"]),
            ("AI 放大人，不是取代人", ["讓 AI 處理例行工作、減少旅程中的摩擦。", "人才能專注在最擅長的事：創意、同理、建立關係、好奇心。"]),
            ("AI 出錯，就是品牌出錯", ["AI 成為品牌的一部分後，顧客分不清演算法和品牌。", "AI 犯錯，顧客只會覺得「這個品牌讓我失望」，接著是負面口碑。"]),
            ("別只量「自動化了多少」", ["自動互動次數、回應時間、內容產量都重要。", "但它們回答不了一個問題：顧客覺得這次互動有意義嗎？"]),
        ],
        "frameworks": [
            ("AI 改變行銷的三個階段", [("table", ["階段", "AI 做什麼"], [["傳統 AI", "分析、預測、優化，幫行銷人做更好的決策"], ["生成式 AI", "創作、對話、個人化，產出新內容"], ["代理式 AI", "決策、執行，自主完成過去由行銷人做的事"]]),
                                      ("p", ["講者強調：能力更強，不等於互動更深。"]),
                                      ("img", "6211", "AI is changing what marketing can do")]),
            ("顧客互動的四種價值", [("table", ["價值", "說明"], [["認知", "AI 分析、預測、優化，幫顧客做決定"], ["情感", "激發熱情，和品牌產生有意義的連結"], ["行為", "讓顧客行動、參與、推薦"], ["關係", "累積忠誠度和長期承諾"]]),
                                  ("p", ["AI 要以顧客為中心來設計，而不是以技術為中心。"])]),
            ("Heartificial 智慧：AI 能力 × 人的能力", [("table", ["人的能力", "AI 做的", "人做的"], [["創意", "幾秒產出上千個點子", "判斷哪些點子值得做"], ["同理", "找出行為模式", "理解顧客真正重視、感受到什麼"], ["好奇", "產出可能的答案", "問出對的問題，挑戰既有假設"], ["判斷", "越來越能自主行動", "決定哪些該自動化、哪些該強化、哪些留給人"]]),
                                                   ("p", ["人的能力沒有變得不重要，反而更重要，只是角色在改變。", "行銷人要清楚：什麼時候用 AI、什麼時候挑戰 AI、什麼時候不用 AI。"]),
                                                   ("img", "6212", "AI capability × Human capability"),
                                                   ("img", "6213", "The human capabilities become more valuable")]),
            ("代理式 AI 時代要問的四個問題", [("ol", ["哪些任務該交給 AI，哪些不該？", "顧客應該保有多少控制權？", "AI 的決策過程，要對顧客多透明？", "品牌怎麼透過 AI，創造有意義的互動？"])]),
            ("讓 AI 更有溫度的四個原則", [("table", ["原則", "做法"], [["強化，不只是自動化", "AI 接手例行工作，把人力留給創意、同理、關係"], ["有目的地個人化", "先調查顧客最重視什麼，只在那些接觸點個人化。創造價值，不是為了監控而監控"], ["保留顧客的自主權", "讓顧客可以選擇不走自動流程；關鍵時刻或服務出錯時，能轉接真人"], ["讓 AI 經營關係", "不只處理一次性交易，要建立信任、延續性和情感連結"]]),
                                        ("p", ["講者也提出四個檢核點：價值、自主、關係、人性。"]),
                                        ("img", "6214", "How can marketers make AI more heartificial?")]),
            ("效率 vs 意義", [("table", ["", "誰負責", "作用"], [["效率", "AI", "讓顧客順利走完旅程"], ["意義", "人", "給顧客留下來的理由"]]),
                             ("p", ["在選擇很多的品類裡，意義帶來忠誠。", "一段完美優化的旅程，仍可能冰冷、讓人記不住。"])]),
        ],
        "quotes": [["能力更強，", "不等於互動更深。"], ["AI 優化體驗，", "人賦予意義。"], ["贏的品牌，不是 AI 用得最多的，", "而是用 AI 變得更有人味的。"]],
        "cases": [
            ("講者的結尾提問", [("aside", ["這場以觀念為主，沒有具體的品牌案例。"]),
                                ("p", ["如果 AI 能處理越來越多行銷工作，", "你會選擇讓品牌裡的人，專注做什麼？"]),
                                ("p", ["講者的答案：不抗拒 AI，也不盲目採用。", "善用 AI 的能力，再補上讓體驗有意義的人性。"]),
                                ("img", "6215", "The heartificial question")]),
        ],
        "actions": [
            ("媒體企劃", [["個人化要有目的。", "先找出顧客最重視的接觸點，只在那些地方做個人化，", "不要每個版位都做。"],
                         ["KPI 除了曝光、互動次數，", "也要看顧客是否回訪、是否留下來。", "效率指標之外，加上關係指標。"],
                         ["用 AI 自動化例行工作，例如報表、排期、優化，", "把時間留給洞察和策略。"]]),
            ("客戶服務", [["幫客戶導入 AI 客服或 AI 代理時，", "保留轉接真人的出口，也讓顧客可以選擇不用自動流程。"],
                         ["AI 出錯會被當成品牌出錯。", "上線前先和客戶講清楚：AI 能做什麼、不能做什麼。"]]),
            ("全體", [["用四個檢核點審視 AI 專案：", "有沒有創造價值？有沒有保留顧客自主？", "有沒有經營關係？有沒有人性？"]]),
        ],
    },
    {
        "id": "n1028-06", "bio": ["OMD Resolution 執行長，Resolution 是俄羅斯 OMD OM Group 旗下的數位單位。", "2023 年起負責 OMD Resolution 的策略產品開發；之前曾任俄羅斯郵政廣告業務負責人、OMD OM Group 行銷科技總監。", "本場同時代表俄羅斯傳播代理商協會（AKAR）。"], "bio_src": "Sostav、AdIndex、大會講者頁",
        "day": "10/28 WED", "time": "15:35–15:55",
        "title": "Artificial intelligence as the partner, opponent, inevitability and hype",
        "speaker": "Sergey Efimov", "role": "OMD Resolution（俄羅斯）執行長",
        "kicker": "",
        "index": [("從跟上到選擇", "選項太多，難的是做決定、扛責任"), ("在地 AI", "全球 AI 不懂在地語言和文化"),
                  ("報表 -90%", "AI 接手例行報表，人專注策略"), ("動機分眾", "同一個年齡層，有六種不同動機"),
                  ("合成樣本", "受眾研究從幾週縮到幾小時")],
        "summary": [
            ("行銷的難題，從「跟上」變成「選擇」", ["以前，媒體代理商忙著跟上不斷湧進的工作。", "現在選項太多，難的是：選哪一個？誰為決策負責？出錯誰扛？"]),
            ("全球 AI，不懂在地", ["數學、法規、商業環境，全球 AI 都處理得很好。", "但在地語言的細節、文化脈絡、具代表性的在地數據，它常常做不好。", "所以俄羅斯的大型科技公司，都在開發自己的 LLM。"]),
            ("行銷人，偏好全球工具", ["在俄羅斯的廣告行銷圈，ChatGPT 使用率 81%、Claude 50%。", "即使這些工具都沒有在俄羅斯正式販售。"]),
            ("AI 有一部分，就是在取代人", ["OMD 用 AI 自動化報表，報表時間減少 90%。", "全公司的成本和人力減少 30%。", "講者直言：AI 有一部分就是取代，而且能帶來實際的商業成果。"]),
            ("AI 不是萬靈丹", ["人的行為太複雜，LLM 的知識又來自過去。", "人本來就難以預測，這正是行銷迷人的地方。"]),
        ],
        "frameworks": [
            ("昨天 vs 今天", [("table", ["", "行銷人面對的問題"], [["昨天", "怎麼跟上？"], ["今天", "選哪個選項？誰為決策負責？出錯誰負責？怎麼確認點子真的可行？"]]),
                            ("img", "6216", "When you have multiple choice of reasonable decisions")]),
            ("全球 AI 的強項與弱項", [("table", ["沒問題", "有問題"], [["數學與數據分析", "理解在地語言的細節"], ["法律、法規", "跟上文化脈絡"], ["市場和商業環境", "符合在地的社交溝通習慣"], ["", "用具代表性的在地數據下結論"]]),
                                    ("img", "6217", "Marketing combines global and local tasks")]),
            ("2026 年俄羅斯的 AI 使用版圖", [("table", ["領域", "主流工具", "特色"], [["日常使用", "Alice AI（Yandex）14.3%、DeepSeek 9.4%、GigaChat 4.0%、ChatGPT 3.5%", "本地、平價或免費的模型最受歡迎"], ["企業使用", "Yandex AI Studio、GigaChat（Sber）、MWS GPT（MTS）", "受法規限制，以本地產品為主"], ["廣告行銷", "ChatGPT 81%、Claude 50%、DeepSeek 39%、Gemini 35%、Perplexity 34%", "以全球工具為主，雖然都沒有在俄羅斯正式販售"]]),
                                           ("aside", ["日常使用的數字是每月觸及率（12 歲以上），廣告行銷的數字是使用比例調查。"]),
                                           ("img", "6218", "AI services usage in Russia in 2026")]),
            ("AI 在代理商的四種用途", [("ol", ["流程自動化", "軟體開發和寫程式", "受眾研究", "生成式 AI 做創意製作"]),
                                     ("p", ["講者分享了前三種的經驗。"])]),
            ("ResoHelper 報表平台怎麼運作", [("flow", ["資料來源", "整理與去重", "持續補充數據", "報表與分析"], 3),
                                            ("ul", ["讀 email：直接從廠商、團隊、客戶的 email 裡抓出成效數字。沒有 API 的平台也能用。", "變更紀錄：每檔活動都有一份變更紀錄，讓 AI 知道發生過什麼，分析才會準確。", "對話：可以直接問系統，上週或上個月有什麼重要變化。"]),
                                            ("img", "6219", "ResoHelper 系統架構"),
                                            ("img", "6220", "Why AI?")]),
            ("合成樣本（Synthetic panel）", [("p", ["用 AI 代理扮演具代表性的顧客角色，可以直接訪問他們。"]),
                                             ("table", ["項目", "說明"], [["避免幻覺", "同一個問題重跑上百次、剔除離群值，回答一致性超過 90%"], ["數據來源", "只用公開數據，數字都要經過外部資料驗證"], ["用途", "評估創意、預測對特定商品的反應、找出接觸點和時機"], ["速度", "傳統焦點團體要幾週，現在 15 分鐘到 2 小時"]]),
                                             ("img", "6222", "Synthetic panel as the new way for audience research")]),
            ("AI 不是萬靈丹的三個原因", [("table", ["原因", "說明"], [["消費行為比想像中複雜", "收集了再多數據，也沒有任何決策能保證結果"], ["LLM 的知識來自過去", "未來總會出現前所未有的變數，需要人即時判斷"], ["人本來就難以預測", "AI 模仿人的思考，但行銷面對的是隨性、多變的喜好"]]),
                                       ("img", "6223", "AI is not a panacea for marketing")]),
        ],
        "quotes": [["我們不只自動化了報表，", "也改變了人在流程中的角色。"], ["LLM 的知識來自過去，", "但未來總會出現前所未有的變數。"]],
        "cases": [
            ("ResoHelper：OMD 的 AI 報表平台", [("ul", ["背景：俄羅斯人才短缺。人口減少，年輕人又偏好內容創作和 IT，代理商很難招到初階人員。", "問題：五分之一的工時花在例行報表。多數廣告平台沒有 API，報表大多是 Excel 檔。", "做法：4 個月從零打造平台，自動讀取廠商報表、統一格式、填入客戶的報表範本。經理設定一次活動約 15 分鐘，之後全自動。"]),
                                               ("stats", [("-90%", "報表準備時間，一份報表只要 2 分鐘"), ("1,370 小時", "8 月單月省下的工時"), ("2,500%", "投資報酬率（ROI）")]),
                                               ("ul", ["規模：支援 30 多名員工、50 個客戶、140 檔活動。", "組織：從「初階專員＋經理」的層級，變成人數更少、專業更高的導師制。", "結果：全公司成本和人力減少 30%，省下相當於 20% 的薪資預算。"])]),
            ("Azelic 抗痘藥：一個年齡層，六種動機", [("ul", ["背景：品類領導品牌 Azelic，市場被低價競品搶走。", "做法：目標從 20–45 歲，縮小到 18–25 歲。這是品牌偏好成形、也最容易換品牌的時期。", "AI 分析：用 AI 顧客旅程代理，分析搜尋行為、內容、評論、決策情境、阻礙和觸發點。"]),
                                                   ("p", ["結果發現，同一個年齡層背後有六種動機："]),
                                                   ("ol", ["不想再遮遮掩掩自己的皮膚", "對自己的皮膚有自信，想真正改善，而不只是遮瑕", "找到平價、簡單的解決方案", "不想再多一道麻煩的保養程序", "找回對自己的掌控感", "需要立即、明確的自信"]),
                                                   ("ul", ["執行：六種動機，變成六套溝通情境（洞察、訊息、創意、接觸時機）。用 DMP 和第三方數據，在搜尋、情境廣告、創作者、影音、電商找到這些族群。", "驗證：用銀行數據做銷售提升分析，找出真正帶動購買的動機。"]),
                                                   ("stats", [("+9 個百分點", "品牌考慮度"), ("+40%", "活動期間銷售年成長，超標 5%"), ("+25%", "活動結束後持續的銷售成長")])]),
        ],
        "actions": [
            ("媒體企劃", [["盤點團隊花在例行報表的工時。", "沒有 API 的平台，也可以用 AI 讀取 Excel 和 email 裡的數據。"],
                         ["每檔活動建立「變更紀錄」。", "記下預算調整、素材替換、版位異動，", "AI 分析成效時才有脈絡。"],
                         ["受眾不要只用年齡切。", "用 AI 分析搜尋、評論、內容，找出同一族群裡的不同動機，", "再分別規劃訊息和接觸時機。"],
                         ["提案前，可以先用合成樣本快速測試創意和接觸點。", "正式決策前，仍要用真實數據驗證。"]]),
            ("數據", [["用全球 AI 處理台灣市場時，", "要補上具代表性的在地數據，並檢查語言和文化細節。"]]),
            ("客戶服務", [["跟客戶溝通 AI 的價值時，用時間和成本說話。", "例如報表時間減少 90%、受眾研究從幾週縮到幾小時。"]]),
        ],
    },
]

NOTE_BY_ID = {n["id"]: n for n in NOTES}

BRAND_SRC = "data:image/png;base64," + base64.b64encode((HERE / "photos" / "heartificial.png").read_bytes()).decode()
BRAND = f'<a class="brand" href="#home" aria-label="回到首頁"><img src="{BRAND_SRC}" alt="DIGIASIA 2026 HEARTIFICIAL Intelligent Marketing"></a>'


def lines(ls):
    return "<br>".join(E(x) for x in ls)


def block(b):
    t = b[0]
    if t == "p":
        return f'<p>{lines(b[1])}</p>'
    if t == "aside":
        return f'<p class="aside">{lines(b[1])}</p>'
    if t == "quote":
        return f'<blockquote class="inline-q">{lines(b[1])}</blockquote>'
    if t == "ol":
        return "<ol class='steps'>" + "".join(f"<li>{E(i)}</li>" for i in b[1]) + "</ol>"
    if t == "ul":
        out = []
        for i in b[1]:
            if "：" in i[:10]:
                k, v = i.split("：", 1)
                out.append(f'<li><span class="lbl">{E(k)}</span>{E(v)}</li>')
            else:
                out.append(f"<li>{E(i)}</li>")
        return "<ul class='facts'>" + "".join(out) + "</ul>"
    if t == "table":
        head = "".join(f"<th>{E(h)}</th>" for h in b[1])
        rows = "".join("<tr>" + "".join(f"<td>{E(c)}</td>" for c in r) + "</tr>" for r in b[2])
        return f'<div class="tbl"><table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>'
    if t == "flow":
        items = "".join(f'<li class="{"hi" if i == b[2] else ""}">{E(x)}</li>' for i, x in enumerate(b[1]))
        return f'<ol class="flow" aria-label="流程">{items}</ol>'
    if t == "img":
        data = base64.b64encode((HERE / "photos" / f"{b[1]}.jpg").read_bytes()).decode()
        return (f'<figure class="shot"><button type="button" class="zoom" aria-label="放大照片">'
                f'<img loading="lazy" src="data:image/jpeg;base64,{data}" alt="{E(b[2])}"></button>'
                f'<figcaption>現場簡報｜{E(b[2])}</figcaption></figure>')
    if t == "stats":
        return '<div class="stats">' + "".join(f'<div class="stat"><b>{E(n)}</b><span>{E(d)}</span></div>' for n, d in b[1]) + "</div>"
    raise ValueError(t)


SECTIONS = [("summary", "快速摘要"), ("frameworks", "核心框架"), ("quotes", "金句摘錄"), ("cases", "案例故事"), ("actions", "行動清單")]


def note_view(n, prev_n, next_n):
    sid = n["id"]
    nav = "".join(f'<a href="#{sid}" data-jump="{sid}-{k}">{E(lbl)}</a>' for k, lbl in SECTIONS)
    idx = "".join(f'<li><b>{E(k)}</b><span>{E(v)}</span></li>' for k, v in n["index"])
    bio = ""
    if n.get("bio"):
        bio = f'<div class="head-bio"><span class="eyebrow">講者背景</span><p>{lines(n["bio"])}</p><p class="src">資料來源：{E(n.get("bio_src",""))}</p></div>'
    summary = "".join(f'<div class="sum"><span class="num">{i}</span><div><h3>{E(h)}</h3><p>{lines(ls)}</p></div></div>' for i, (h, ls) in enumerate(n["summary"], 1))
    fw = "".join(f'<div class="fw"><h3><span class="tag">框架{"一二三四五六七八"[i]}</span>{E(t)}</h3>' + "".join(block(b) for b in bs) + "</div>" for i, (t, bs) in enumerate(n["frameworks"]))
    quotes = "".join(f'<blockquote class="q">{lines(q)}</blockquote>' for q in n["quotes"])
    cases = "".join(f'<div class="case"><h3>{E(t)}</h3>' + "".join(block(b) for b in bs) + "</div>" for t, bs in n["cases"])
    acts = "".join(f'<div class="act"><h3><span class="role">{E(r)}</span></h3><ul>' + "".join(f"<li>{lines(it)}</li>" for it in items) + "</ul></div>" for r, items in n["actions"])
    body = {"summary": summary, "frameworks": fw, "quotes": f'<div class="quotes">{quotes}</div>', "cases": cases, "actions": acts}
    secs = "".join(f'<section class="part" id="{sid}-{k}"><h2>{E(lbl)}</h2>{body[k]}</section>' for k, lbl in SECTIONS)
    pager = '<nav class="pager">'
    pager += f'<a href="#{prev_n["id"]}"><small>上一場</small>{E(prev_n["speaker"])}</a>' if prev_n else "<span></span>"
    pager += '<a href="#home" class="mid"><small>回到</small>全部場次</a>'
    pager += f'<a href="#{next_n["id"]}" class="nx"><small>下一場</small>{E(next_n["speaker"])}</a>' if next_n else "<span></span>"
    pager += "</nav>"
    return f'''
<div class="view" data-view="{sid}" hidden>
  <header class="note-head"><div class="wrap">
    {BRAND}
    <a class="back" href="#home">← 全部場次</a>
    <p class="meta"><span class="mono">{E(n["day"])}　{E(n["time"])}</span><span>{E(n.get("kicker",""))}</span></p>
    <h1>{E(n["title"])}</h1>
    <p class="who"><b>{E(n["speaker"])}</b>{E(n["role"])}</p>
    {bio}
  </div></header>
  <nav class="tabs"><div class="wrap">{nav}</div></nav>
  <div class="wrap note-grid">
    <aside class="side">
      <div class="idx"><span class="eyebrow">重點索引</span><ul>{idx}</ul></div>
    </aside>
    <main class="content">{secs}{pager}</main>
  </div>
</div>'''


def home_view():
    days = ""
    for key, (d, wd, rows) in SCHEDULE.items():
        items = ""
        for time, title, who, st in rows:
            if isinstance(st, list):
                links = "".join(f'<a class="chip done" href="#{i}">{(E(NOTE_BY_ID[i]["speaker"].split(" ")[0]) + " ") if len(st) > 1 else ""}講座筆記精華&gt;&gt;</a>' for i in st)
                items += f'<li class="row has"><span class="t mono">{E(time)}</span><div class="ti"><a class="tl" href="#{st[0]}">{E(title)}</a><span class="sp">{E(who)}</span></div><div class="st">{links}</div></li>'
            else:
                chip = '<span class="chip skip">略過</span>' if st == "skip" else '<span class="chip wait">待整理</span>'
                items += f'<li class="row{" off" if st == "skip" else ""}"><span class="t mono">{E(time)}</span><div class="ti"><span class="tl">{E(title)}</span><span class="sp">{E(who)}</span></div><div class="st">{chip}</div></li>'
        days += f'<section class="day"><h2><span class="mono">{d}</span><small>{wd}</small></h2><ul class="sched">{items}</ul></section>'
    done = sum(1 for n in NOTES)
    return f'''
<div class="view" data-view="home">
  <header class="home-head"><div class="wrap">
    {BRAND}
    <p class="eyebrow">DIGIASIA 2026 數位亞洲大會</p>
    <h1>講座筆記</h1>
    <p class="lede">依時間排列。每場筆記分成快速摘要、核心框架、金句摘錄、案例故事、行動清單五個部分，行動清單以媒體企劃為主。</p>
    <p class="count"><span class="mono">{done}</span> 份筆記已整理，其餘場次陸續更新。</p>
  </div></header>
  <div class="wrap days">{days}</div>
</div>'''


CSS = (HERE / "style.css").read_text()
JS = (HERE / "app.js").read_text()

views = home_view()
for i, n in enumerate(NOTES):
    views += note_view(n, NOTES[i - 1] if i > 0 else None, NOTES[i + 1] if i + 1 < len(NOTES) else None)

page = f'''<title>DIGIASIA 2026 講座筆記</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;900&family=Silkscreen&family=IBM+Plex+Mono:wght@500&display=swap">
<style>{CSS}</style>
{views}
<script>{JS}</script>
'''
(HERE / "digiasia-notes.html").write_text(page)
print("ok", len(page))


def md_lines(ls):
    return "\n".join(ls)


def md_block(b):
    t = b[0]
    if t in ("p", "aside"):
        return md_lines(b[1])
    if t == "quote":
        return "> " + "".join(b[1])
    if t == "ol":
        return "\n".join(f"{i}. {x}" for i, x in enumerate(b[1], 1))
    if t == "ul":
        return "\n".join(f"- {x}" for x in b[1])
    if t == "table":
        h = "| " + " | ".join(b[1]) + " |\n|" + "---|" * len(b[1])
        return h + "\n" + "\n".join("| " + " | ".join(r) + " |" for r in b[2])
    if t == "flow":
        return " → ".join(b[1])
    if t == "stats":
        return "\n".join(f"- {n}：{d}" for n, d in b[1])
    if t == "img":
        return f"（現場簡報照片：{b[2]}）"
    return ""


def note_md(n):
    out = [f"# {n['day']}　{n['time']}｜{n['speaker']}", "", f"**{n['role']}**", f"**{n['title']}**"]
    if n.get("kicker"):
        out.append(f"（{n['kicker']}）")
    if n.get("bio"):
        out += ["", "> 講者背景"] + [f"> {x}" for x in n["bio"]] + [f"> （資料來源：{n.get('bio_src','')}）"]
    out += ["", "---", "", "## 重點索引", "", "| 關鍵詞 | 說明 |", "|---|---|"] + [f"| {k} | {v} |" for k, v in n["index"]]
    out += ["", "---", "", "## 快速摘要", ""]
    for i, (h, ls) in enumerate(n["summary"], 1):
        out += [f"**{i}. {h}**", md_lines(ls), ""]
    out += ["---", "", "## 核心框架", ""]
    for i, (t, bs) in enumerate(n["frameworks"]):
        out += [f"**框架{'一二三四五六七八'[i]}：{t}**", ""]
        for b in bs:
            out += [md_block(b), ""]
    out += ["---", "", "## 金句摘錄", ""]
    for q in n["quotes"]:
        out += ["> " + "".join(q), ""]
    out += ["---", "", "## 案例故事", ""]
    for t, bs in n["cases"]:
        out += [f"**{t}**"]
        for b in bs:
            out += [md_block(b)]
        out += [""]
    out += ["---", "", "## 行動清單", ""]
    for role, items in n["actions"]:
        out += [f"**{role}**"] + ["- " + "".join(it) for it in items] + [""]
    return "\n".join(out)


MD_NAMES = {"n1028-01": "1028-01-林友琴", "n1028-01b": "1028-01b-佐佐木康晴", "n1028-02": "1028-02-王俞蓉", "n1028-03": "1028-03-Bharat-Avalani", "n1028-04": "1028-04-Fredrik-Borestrom", "n1028-05": "1028-05-Linda-Hollebeek", "n1028-06": "1028-06-Sergey-Efimov"}
(HERE / "md").mkdir(exist_ok=True)
for n in NOTES:
    name = MD_NAMES.get(n["id"], n["id"])
    (HERE / "md" / f"{name}.md").write_text(note_md(n))
