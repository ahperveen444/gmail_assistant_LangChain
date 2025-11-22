# Imports needed
from langchain_community.agent_toolkits import GmailToolkit
from langchain_community.tools.gmail.utils import(
    build_resource_service,
    get_gmail_credentials,
)
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Setting Gmail Credentials
credentials_gmail = get_gmail_credentials(
    token_file="token.json",
    scopes=["https://mail.google.com/"],
    client_secrets_file="credentials2.json",
)
api_resource_gmail = build_resource_service(credentials=credentials_gmail)

# Using Gmail tools using GmailToolkit
toolkit_gmail = GmailToolkit(api_resource=api_resource_gmail)
tools_gmail = toolkit_gmail.get_tools()

# Defining our model
model = ChatOpenAI(model = "gpt-3.5-turbo")

# Defining our prompt
prompt = PromptTemplate(
 template="""You are a professional email assistant. My name is Ali Haider. You will write email in a professional, friendly tone which user will ask you to do. Here is user prompt:
 {query}.
 """,
 input_variables=['query']
)

# tool binding
llm_with_tool = model.bind_tools(tools_gmail)
query = input("Enter : ")

#chain
chain = prompt | llm_with_tool

response = chain.invoke(query)

# print(response)

# list of tools into name
tool_map = {t.name: t for t in tools_gmail}

# tool calls
if response.tool_calls:
    for call in response.tool_calls:
        tool_name = call["name"]
        tool_args = call["args"]

        tool = tool_map[tool_name]

        # execute tool
        result = tool.invoke(tool_args)
        print("Action Completed Successfully")
else:
    print("No tool calls.")


