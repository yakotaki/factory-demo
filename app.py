from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


TEXTS = {
    "en": {
        "site_title": "Shanghai Bright Tools Co., Ltd. | Hand Tools Manufacturer in China",
        "brand": "Bright Tools",

        "nav_factory": "Factory",
        "nav_products": "Products",
        "nav_quality": "Quality",
        "nav_shipping": "Shipping",
        "nav_faq": "FAQ",
        "nav_contact": "Inquiry",

        "language_label": "Language",

        "hero_title": "Reliable Hand Tools from Shanghai, China — Shipped Worldwide",
        "hero_lead": (
            "Shanghai Bright Tools Co., Ltd. is a professional manufacturer and OEM supplier of "
            "hand tools and hardware for brands and importers in Europe, North America, and other markets."
        ),
        "hero_intro2": (
            "We focus on stable quality, on-time delivery, and clear English communication to make your "
            "sourcing from China easier and safer."
        ),
        "hero_cta_quote": "Request a Quote",
        "hero_cta_view": "View Product Range",
        "hero_moq": "MOQ-friendly · OEM / ODM service",

        "quick_facts_title": "Quick Facts",
        "quick_years_number": "12+",
        "quick_years_label": "Years of production",
        "quick_countries_number": "35+",
        "quick_countries_label": "Export countries",
        "quick_iso_number": "ISO",
        "quick_iso_label": "Quality management",
        "quick_leadtime_number": "7–30",
        "quick_leadtime_label": "Days typical lead time",
        "quick_oem_line": "OEM & private label for tool brands, supermarkets, importers and distributors.",

        "section_about_title": "About Shanghai Bright Tools",

        "about_p1": (
            "Shanghai Bright Tools Co., Ltd. is located close to Shanghai Port, one of the largest seaports "
            "in China. We specialize in the production and export of hand tools including socket sets, "
            "wrenches, screwdrivers, pliers, and related hardware."
        ),
        "about_p2": (
            "Our factory works with both international brands and local trading companies. "
            "We can supply under your own brand (OEM) or develop new items together (ODM). "
            "Each order is followed carefully from raw materials, through production, "
            "to final inspection before shipment."
        ),
        "about_p3": (
            "We welcome small trial orders to test our quality and service before long-term cooperation."
        ),
        "about_key_title": "Key Advantages",
        "about_key_1": "Convenient location near Shanghai Port",
        "about_key_2": "Flexible MOQ for new customers",
        "about_key_3": "OEM / ODM and custom packaging",
        "about_key_4": "English-speaking sales team",
        "about_key_5": "Stable cooperation with certified subcontractors",

        "section_products_title": "Main Product Categories",
        "products_intro": (
            "Below are our typical product groups. For detailed specifications and catalog, "
            "please contact us and we will send you our latest PDF catalog."
        ),

        "product1_badge": "Socket & Ratchet Sets",
        "product1_title": "Socket & Ratchet Sets",
        "product1_text": (
            "Chrome-vanadium socket sets in blow-mold cases, 1/4\", 3/8\", 1/2\" drive, "
            "suitable for automotive and DIY markets. Custom combinations and branding available."
        ),
        "product1_li1": "CR-V / carbon steel",
        "product1_li2": "Metric and imperial sizes",
        "product1_li3": "Custom color cases and labels",

        "product2_badge": "Wrenches & Spanners",
        "product2_title": "Wrenches & Spanners",
        "product2_text": (
            "Combination wrenches, adjustable wrenches, ratcheting wrenches for "
            "hardware stores, supermarkets, and professional markets."
        ),
        "product2_li1": "Mirror, satin, or black finish",
        "product2_li2": "Individual blister or set packing",
        "product2_li3": "EN / DIN standards on request",

        "product3_badge": "Screwdrivers & Pliers",
        "product3_title": "Screwdrivers & Pliers",
        "product3_text": (
            "Standard and precision screwdrivers, combination pliers, long nose pliers, "
            "and other common hand tools for general use."
        ),
        "product3_li1": "Non-slip handles with your colors",
        "product3_li2": "Set combinations for DIY kits",
        "product3_li3": "Hanging card / boxed / bag packing",

        "products_cta_button": "Ask for Full Catalog (PDF)",
        "products_cta_hint": (
            "Tell us your target market and quality level — we will recommend suitable items."
        ),

        # QUALITY
        "section_quality_title": "Quality Control & Certificates",
        "quality_p1": (
            "Quality is controlled step by step: incoming raw material inspection, in-process checks, "
            "and final inspection before packing. We keep test records for each batch."
        ),
        "quality_p2": (
            "On request, we can cooperate with third-party inspection companies such as SGS, TÜV, "
            "or your nominated agent. Samples can be tested according to your standard."
        ),
        "quality_p3": (
            "We are familiar with requirements from European and North American markets and can help you "
            "prepare the necessary documents on the tool side."
        ),
        "quality_docs_title": "Typical Documents",
        "quality_doc_li1": "Material certificates (CR-V, etc.)",
        "quality_doc_li2": "Hardness and torque test reports",
        "quality_doc_li3": "Dimensional inspection reports",
        "quality_doc_li4": "Packing list & detailed carton markings",
        "quality_docs_note": (
            "Detailed certificates can be prepared according to your project requirements."
        ),

        # SHIPPING
        "section_shipping_title": "Shipping & Lead Time",
        "shipping_p1": (
            "We usually ship from Shanghai Port, but Shanghai Port is also possible. "
            "For standard items with our existing molds and packing, lead time is normally:"
        ),
        "shipping_li1": "Sample order: around 7–10 days",
        "shipping_li2": "Trial order: around 20–25 days",
        "shipping_li3": "Regular repeat orders: around 30–40 days",
        "shipping_p2": "Exact delivery time depends on order quantity, packing requirements, and season.",
        "shipping_payment_title": "Payment Terms (for sample demo)",
        "shipping_payment_li1": "New customers: 30% T/T deposit, 70% balance before shipment",
        "shipping_payment_li2": "Long-term partners: to be discussed",
        "shipping_payment_li3": "Small sample orders: payment in advance",
        "shipping_payment_note": (
            "We work flexibly with customers and are open to discussing other reasonable terms."
        ),

        # FAQ
        "section_faq_title": "Frequently Asked Questions",
        "faq_q1": "Q1: What is your minimum order quantity (MOQ)?",
        "faq_a1": (
            "A1: For most items, our standard MOQ is one full carton per size. "
            "For trial orders or new items we can be more flexible. "
            "Please tell us which market you sell to."
        ),
        "faq_q2": "Q2: Can you produce under our brand and design?",
        "faq_a2": (
            "A2: Yes. We can print your logo on tools, cases, and packing, "
            "and follow your brand guidelines for colors and artwork."
        ),
        "faq_q3": "Q3: Do you provide samples?",
        "faq_a3": (
            "A3: Samples can be provided for quality checking. Some items are free; "
            "for others we charge sample cost plus freight."
        ),
        "faq_q4": "Q4: Can you arrange third-party inspection?",
        "faq_a4": (
            "A4: Yes. We can cooperate with SGS, TÜV or your own appointed inspection company. "
            "The inspection cost is normally paid by the buyer."
        ),

        # CONTACT
        "section_contact_title": "Contact & Inquiries",
        "contact_intro": (
            "For inquiries, please send us your product list or photos, target market, and approximate "
            "quantity. We will reply with suggestions and a quotation."
        ),
        "contact_company_label": "Company:",
        "contact_address_label": "Address:",
        "contact_email_label": "Email:",
        "contact_phone_label": "Phone / WeChat:",
        "contact_demo_note": (
            "This is a demo website used to show the style of export websites we can build "
            "for factories and trading companies in China."
        ),

        "form_name_label": "Your Name",
        "form_name_placeholder": "Your full name",
        "form_company_label": "Company",
        "form_company_placeholder": "Company name",
        "form_email_label": "Email",
        "form_email_placeholder": "you@example.com",
        "form_message_label": "Message",
        "form_message_placeholder": (
            "Tell us what tools you need, target market, and quantity."
        ),
        "form_submit": "Send Inquiry",

        "footer_demo": "Demo website for export web design services",
    },

    "zh": {
        "site_title": "上海光辉工具有限公司 | 中国手工具制造商",
        "brand": "Bright Tools",

        "nav_factory": "工厂介绍",
        "nav_products": "产品",
        "nav_quality": "质量",
        "nav_shipping": "运输",
        "nav_faq": "常见问题",
        "nav_contact": "询盘",

        "language_label": "语言",

        "hero_title": "来自中国上海的可靠手工具——销往全球",
        "hero_lead": (
            "上海光辉工具有限公司是一家专业的手工具和五金制造商与 OEM 供应商，"
            "为欧洲、北美及其他市场的品牌和进口商提供服务。"
        ),
        "hero_intro2": (
            "我们专注于稳定的质量、准时交货以及清晰的英语沟通，让您从中国的采购更轻松、更安全。"
        ),
        "hero_cta_quote": "索取报价",
        "hero_cta_view": "查看产品范围",
        "hero_moq": "起订量灵活 · 支持 OEM / ODM",

        "quick_facts_title": "关键信息",
        "quick_years_number": "12+",
        "quick_years_label": "年生产经验",
        "quick_countries_number": "35+",
        "quick_countries_label": "出口国家和地区",
        "quick_iso_number": "ISO",
        "quick_iso_label": "质量管理体系",
        "quick_leadtime_number": "7–30",
        "quick_leadtime_label": "典型交期（天）",
        "quick_oem_line": "为工具品牌、超市、进口商和经销商提供 OEM / 自有品牌服务。",

        "section_about_title": "关于上海光辉工具",

        "about_p1": (
            "上海光辉工具有限公司靠近中国最大的港口之一——上海港，"
            "主要生产和出口手工具，包括套筒组套、扳手、螺丝刀、钳子及相关五金件。"
        ),
        "about_p2": (
            "工厂同时与国际品牌及本地外贸公司合作，"
            "可为您提供自有品牌（OEM）生产，也可以共同开发新产品（ODM）。"
            "每一批订单都从原材料、生产过程到装运前终检进行严格跟踪。"
        ),
        "about_p3": "欢迎通过小批量试订单来了解我们的质量和服务，建立长期合作。",
        "about_key_title": "主要优势",
        "about_key_1": "靠近上海港，出货方便",
        "about_key_2": "对新客户提供灵活的起订量",
        "about_key_3": "支持 OEM / ODM 及定制包装",
        "about_key_4": "英语沟通顺畅的销售团队",
        "about_key_5": "与通过认证的合作工厂长期稳定合作",

        "section_products_title": "主要产品类别",
        "products_intro": (
            "下面是我们常规的产品系列。如需详细规格和目录，请联系我们索取最新 PDF 电子目录。"
        ),

        "product1_badge": "套筒及棘轮组套",
        "product1_title": "套筒及棘轮组套",
        "product1_text": (
            "铬钒钢套筒组套，配吹塑箱，1/4\"、3/8\"、1/2\" 传动，"
            "适用于汽车维修及家用 DIY 市场，可按要求组合及定制品牌。"
        ),
        "product1_li1": "CR-V / 碳钢材质",
        "product1_li2": "公制及英制规格",
        "product1_li3": "可定制箱体颜色和标签",

        "product2_badge": "扳手系列",
        "product2_title": "扳手系列",
        "product2_text": (
            "两用扳手、活动扳手、棘轮扳手等，适用于五金店、超市以及专业市场。"
        ),
        "product2_li1": "镜面、雾面或黑色表面处理",
        "product2_li2": "单支吸塑或成套包装",
        "product2_li3": "可按要求符合 EN / DIN 标准",

        "product3_badge": "螺丝刀及钳类",
        "product3_title": "螺丝刀及钳类",
        "product3_text": (
            "标准及精密螺丝刀、尖嘴钳、钢丝钳等常用手工具，适合一般用途。"
        ),
        "product3_li1": "防滑手柄，可按您的颜色定制",
        "product3_li2": "多种成套组合适合 DIY 套装",
        "product3_li3": "吊卡 / 盒装 / 袋装等多种包装方式",

        "products_cta_button": "索取完整电子目录 (PDF)",
        "products_cta_hint": "请告知您的目标市场和质量档次，我们会推荐合适的产品。",

        # 质量
        "section_quality_title": "质量控制与证书",
        "quality_p1": (
            "我们的质量控制分为多个步骤：原材料进厂检验、生产过程巡检以及包装前最终检验，"
            "并为每一批次保留测试记录。"
        ),
        "quality_p2": (
            "根据客户要求，我们可以配合 SGS、TÜV 等第三方检验机构或您指定的验货公司进行检验，"
            "样品也可按您的标准进行测试。"
        ),
        "quality_p3": (
            "我们熟悉欧洲和北美市场的相关要求，可以协助您准备工具类产品所需的文件资料。"
        ),
        "quality_docs_title": "常见文件",
        "quality_doc_li1": "材料证明（如 CR-V 等）",
        "quality_doc_li2": "硬度及扭矩测试报告",
        "quality_doc_li3": "尺寸检验报告",
        "quality_doc_li4": "装箱单及详细外箱唛头",
        "quality_docs_note": "可根据具体项目需求准备更为详细的证明和报告。",

        # 发货
        "section_shipping_title": "发货与交期",
        "shipping_p1": (
            "我们通常从上海港出货，如有需要也可以从上海港装运。"
            "对于已有模具和包装的常规产品，常见交期如下："
        ),
        "shipping_li1": "样品订单：约 7–10 天",
        "shipping_li2": "试订单：约 20–25 天",
        "shipping_li3": "常规重复订单：约 30–40 天",
        "shipping_p2": "具体交货时间还取决于订单数量、包装要求及旺季情况。",
        "shipping_payment_title": "付款条款（演示用）",
        "shipping_payment_li1": "新客户：预付 30% 电汇订金，出货前付清 70% 余款",
        "shipping_payment_li2": "长期合作客户：可协商更灵活条款",
        "shipping_payment_li3": "小额样品订单：一般需全款预付",
        "shipping_payment_note": (
            "我们在付款方式上较为灵活，欢迎与我们讨论其他合理的合作方案。"
        ),

        # FAQ
        "section_faq_title": "常见问题解答",
        "faq_q1": "问1：你们的起订量是多少？",
        "faq_a1": (
            "答1：大部分产品的标准起订量为每个尺寸至少一箱。"
            "如为试订单或新开发产品，我们可以适当放宽，请告知您销售的市场。"
        ),
        "faq_q2": "问2：可以按照我们的品牌和设计生产吗？",
        "faq_a2": (
            "答2：可以。我们可以在工具本体、工具箱及包装上印刷您的品牌标识，"
            "并按照您的品牌手册制作颜色和设计。"
        ),
        "faq_q3": "问3：可以提供样品吗？",
        "faq_a3": (
            "答3：我们可提供样品用于质量确认，部分产品样品免费，部分产品会收取样品费及运费。"
        ),
        "faq_q4": "问4：可以安排第三方验货吗？",
        "faq_a4": (
            "答4：可以。我们可配合 SGS、TÜV 或您指定的第三方验货公司，验货费用通常由买方承担。"
        ),

        # 联系方式
        "section_contact_title": "联系方式与询盘",
        "contact_intro": (
            "如需询盘，请发送您的产品清单或图片、目标市场以及大致数量，我们会给出建议和报价。"
        ),
        "contact_company_label": "公司：",
        "contact_address_label": "地址：",
        "contact_email_label": "邮箱：",
        "contact_phone_label": "电话 / 微信：",
        "contact_demo_note": (
            "本网页仅为演示网站，用于展示我们为中国工厂和外贸公司制作出口型网站的风格。"
        ),

        "form_name_label": "您的姓名",
        "form_name_placeholder": "请输入您的姓名",
        "form_company_label": "公司",
        "form_company_placeholder": "公司名称",
        "form_email_label": "邮箱",
        "form_email_placeholder": "you@example.com",
        "form_message_label": "留言",
        "form_message_placeholder": "请告诉我们您需要的工具、目标市场及数量。",
        "form_submit": "发送询盘",

        "footer_demo": "出口型网站设计演示页面",
    },
}


def get_lang(default="en"):
    lang = request.args.get("lang", default)
    return "zh" if lang and lang.lower() in ("zh", "cn", "zh-cn") else "en"



@app.route("/")
def home():
    lang = get_lang()
    t = TEXTS[lang]
    return render_template("web1_factory.html", t=t, lang=lang)


@app.route("/samples/factory")
def sample_factory():
    lang = get_lang()
    return redirect(url_for("home", lang=lang))


if __name__ == "__main__":
    app.run(debug=True)
