import win32com.client
import win32com

def outlook_account():
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    accounts = win32com.client.Dispatch("Outlook.Application").Session.Accounts;
    return outlook, accounts

def read_inbox(outlook, accounts):
    for account in accounts:
        inbox = outlook.Folders(account.DeliveryStore.DisplayName)
        inbox_messages = inbox.Folders[1].items
    return inbox_messages

def read_messages(inbox):
    email_list = {str(message.Subject) + "_" + (str(message.SentOn).split(' ')[0]): 0 for message in inbox}
    print("Email list with timestamps: ", email_list)
    for message in inbox:
        # print("Sender email - ID: ", message.SenderEmailAddress)
        # print("Email Subject: ", message.Subject)
        # print("Message sent date: ", message.SentOn)
        email_list[str(message.Subject) + "_" + str(message.SentOn).split(' ')[0]] += 1
    return email_list

if __name__ == "__main__":
    outlook, accounts = outlook_account()
    print("Outlook account holder: ", accounts[0].DisplayName)
    inbox = read_inbox(outlook, accounts)
    print("Total number of messages in Inbox: ", len(inbox))
    email_list_count = read_messages(inbox)
    print(email_list_count)
    # This code gives you the "EmailSubject_Date : CountOfEmailsPerDay" dictionary
    # Once I get the tool codes, I can filter those out using the regex