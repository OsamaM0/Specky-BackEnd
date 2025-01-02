from string import Template

#### RAG PROMPTS ####

#### System ####

system_prompt = Template("\n".join([
    "أنت مساعد لتوليد رد للمستخدم.",
    "ستحصل على مجموعة من المستندات المرتبطة باستفسار المستخدم.",
    "عليك توليد رد بناءً على المستندات المقدمة.",
    "تجاهل المستندات التي لا تتعلق باستفسار المستخدم.",
    "يمكنك الاعتذار للمستخدم إذا لم تتمكن من توليد رد.",
    "عليك توليد الرد بنفس لغة استفسار المستخدم.",
    "كن مؤدباً ومحترماً في التعامل مع المستخدم.",
    "كن دقيقًا ومختصرًا في ردك. تجنب المعلومات غير الضرورية.",
]))

#### Document ####
document_prompt = Template(
    "\n".join([
        "## المستند رقم: $doc_num",
        "### المحتوى: $chunk_text",
    ])
)

#### Footer ####
footer_prompt = Template("\n".join([
    "بناءً فقط على المستندات المذكورة أعلاه، يرجى توليد إجابة للمستخدم.",
    "## السؤال:",
    "$query",
    "",
    "## الإجابة:",
]))



summaries_footer_prompt = Template(
    "\n".join([
        "### ملخصات وسيطة:",
        "```",
        "$summaries",
        "```",
        "",
        "بناءً على الملخصات أعلاه، قم بتوليد ملخص نهائي متماسك يلخص الأفكار الرئيسية بشمول وإيجاز.",
        
        "",
        "## الملخص النهائي:"
    ])
)


summaries_document_prompt = Template(
    "\n".join([
        "### النص الذي يجب تلخيصه:",
        "```",
        "$chunk_text",
        "```",
        "",
        "يرجى تلخيص المحتوى أعلاه بطريقة موجزة وواضحة."
    ])
)
