# This is a configuration for uniquely similar messages.

# Uniquely by regex.
regex = [
	"[0-9]"
]

# Uniquely by cutting off the part of the message that follows the specified messages.
split = [
	"MessageId =",
	"message id =",
	"Message processing error",
	"messageId=ID",
	"xsd-схеме (Обработка документа"
]
