import language_tool_python

def grammarCorrector(text):
    tool = language_tool_python.LanguageTool('en-US')
    result = tool.correct(text)
    tool.close()
    return result