messages = [
    {
        'source': 'ru.atc.carcass.common.exception.FaultException: Client error while calling esia oss, orderId = 1709396281, statusCode = 400, statusText = , body = {"reason":"ERROR: duplicate key value violates unique constraint \"claim_oph_unq\"\n',
        'target': 'ru.atc.carcass.common.exception.FaultException: Client error while calling esia oss, orderId = [[target]], statusCode = 400, statusText = , body = {"reason":"ERROR: duplicate key value violates unique constraint',
        'pseudo': 'Ошибка, которую добавил Я - Ярослав'
    },
    {
        'source': 'Какой-то текст ошибки с id = 546416.8sdf16sfv651 и дальше идет еще текст"}',
        'target': 'Какой-то текст ошибки с id = [[target]] и дальше идет еще текст',
        'pseudo': 'Ошибка_0 текст в отчет'
    },
    {
        'source': '''ru.atc.carcass.common.exception.FaultException: Error while calling esia for orderId = 1718647484, statusCode = 400, statusText = , body = {"reason":"Request body is not correct. JSON parse error: Cannot deserialize value of type `ru.gosuslugi.esia.corpo.model.CorpoStatus` from String \"NOT_VERIFIED\": not one of the values accepted for Enum class: [VERIFIED]; nested exception is com.fasterxml.jackson.databind.exc.InvalidFormatException: Cannot deserialize value of type `ru.gosuslugi.esia.corpo.model.CorpoStatus` from String \"NOT_VERIFIED\": not one of the values accepted for Enum class: [VERIFIED]\n at [Source: (PushbackInputStream); line: 1, column: 388] (through reference chain: java.util.ArrayList[0]->ru.gosuslugi.esia.corpo.model.CorpoEntity[\"docStatus\"])"}''',
        'target': 'ru.atc.carcass.common.exception.FaultException: Error while calling esia for orderId = [[target]], statusCode = 400, statusText = , body = {"reason":"Request body is not correct. JSON parse error: Cannot deserialize value of type `ru.gosuslugi.esia.corpo.model.CorpoStatus` from String \"NOT_VERIFIED\": not one of the values accepted for Enum class: [VERIFIED]; nested exception is com.fasterxml.jackson.databind.exc.InvalidFormatException: Cannot deserialize value of type `ru.gosuslugi.esia.corpo.model.CorpoStatus` from String \"NOT_VERIFIED\": not one of the values accepted for Enum class: [VERIFIED]\n at [Source: (PushbackInputStream); line: 1, column: 388] (through reference chain: java.util.ArrayList[0]->ru.gosuslugi.esia.corpo.model.CorpoEntity[\"docStatus\"])"}',
        'pseudo': 'Ошибка_1'
    },
    {
        'source': 'ru.atc.carcass.common.exception.FaultException: Error while calling esia for orderId = 1718581499, statusCode = 400, statusText = , body = {"reason":"ERROR: duplicate key value violates unique constraint \"claim_oph_unq\"\n  Detail: Key (claim_num, oph)=(1718581499, +7(967)3749397) already exists.","code":"CRP-400"}',
        'target': 'ru.atc.carcass.common.exception.FaultException: Error while calling esia for orderId = [[target]], statusCode = 400, statusText = , body = {"reason":"ERROR: duplicate key value violates unique constraint \"claim_oph_unq\"\n  Detail: Key (claim_num, oph)=([[target]], [[target]] already exists.","code":"CRP-400"}',
        'pseudo': 'Ошибка_2'
    },
    {
        'source': 'ru.atc.carcass.common.exception.FaultException: Client error while calling esia oss, orderId = 1717888407, statusCode = 400, statusText = , body = {"reason":"ClaimNum 1717888407 - simActive may not be empty","code":"CRP-400"}',
        'target': 'ru.atc.carcass.common.exception.FaultException: Client error while calling esia oss, orderId = [[target]], statusCode = 400, statusText = , body = {"reason":"ClaimNum [[target]] - simActive may not be empty","code":"CRP-400"}',
        'pseudo': 'Ошибка_3'
    },
    {
        'source': 'ru.gosuslugi.pgu.core.processing.exception.ProcessingServiceException: FAULTProcessing for messageId=ID:ffabe7ef-7149-11ec-b610-46d5a32231ff, endpoint=http://p00smevlb-vip:7777/gateway/services/SID0003418, serviceCode=10000000101',
        'target': 'ru.gosuslugi.pgu.core.processing.exception.ProcessingServiceException: FAULTProcessing for messageId=ID:[[target]], endpoint=http://p00smevlb-vip:7777/gateway/services/SID0003418, serviceCode=[[target]]',
        'pseudo': 'Ошибка_4'
    },
    {
        'source': 'Smev3CallError{errorCode=ASYNCH_CALL_ERROR, message=\'SMEV-403:Бизнес-данные сообщения не соответствуют схеме, зарегистрированной в СМЭВ. MessageId = 54d5ac8c-714e-11ec-ada4-0a3409f9905c: cvc-pattern-valid: Value \'Уфа г., Коллективный сад N40 ОСТ ОАО УМПО тер.\' is not facet-valid with respect to pattern \'[А-Яа-яЁёMDCLXVI\d\s\(\)\.,;:\-\'"№/]{1,255}\' for type \'Address255Type\'. [-1], cvc-type.3.1.3: The value \'Уфа г., Коллективный сад N40 ОСТ ОАО УМПО тер.\' of element \'Locality\' is not valid. [-1], cvc-pattern-valid: Value \'Уфа г., Коллективный сад N40 ОСТ ОАО УМПО тер.\' is not facet-valid with respect to pattern \'[А-Яа-яЁёMDCLXVI\d\s\(\)\.,;:\-\'"№/]{1,255}\' for type \'Address255Type\'. [-1], cvc-type.3.1.3: The value \'Уфа г., Коллективный сад N40 ОСТ ОАО УМПО тер.\' of element \'Locality\' is not valid. [-1], cvc-pattern-valid: Value \'Уфа г., Коллективный сад N40 ОСТ ОАО УМПО тер.\' is not facet-valid with respect to pattern \'[А-Яа-яЁёMDCLXVI\d\s\(\)\.,;:\-\'"№/]{1,255}\' for type \'Address255Type\'. [-1], cvc-type.3.1.3: The value \'Уфа г., Коллективный сад N40 ОСТ ОАО УМПО тер.\' of element \'Locality\' is not valid. [-1]\', category=\'null\', smevFault=null}',
        'target': 'Smev3CallError{errorCode=ASYNCH_CALL_ERROR, message=\'SMEV-403:Бизнес-данные сообщения не соответствуют схеме, зарегистрированной в СМЭВ. MessageId = [[target]]: cvc-pattern-valid: Value [[target]] is not facet-valid with respect to pattern \'[А-Яа-яЁёMDCLXVI\d\s\(\)\.,;:\-\'"№/]{1,255}\' for type \'Address255Type\'. [-1], cvc-type.3.1.3: The value [[target]] of element \'Locality\' is not valid. [-1], cvc-pattern-valid: Value [[target]] is not facet-valid with respect to pattern \'[А-Яа-яЁёMDCLXVI\d\s\(\)\.,;:\-\'"№/]{1,255}\' for type \'Address255Type\'. [-1], cvc-type.3.1.3: The value [[target]] of element \'Locality\' is not valid. [-1], cvc-pattern-valid: Value [[target]] is not facet-valid with respect to pattern \'[А-Яа-яЁёMDCLXVI\d\s\(\)\.,;:\-\'"№/]{1,255}\' for type \'Address255Type\'. [-1], cvc-type.3.1.3: The value \'[[target]] of element \'Locality\' is not valid. [-1]\', category=\'null\', smevFault=null}',
        'pseudo': 'Ошибка_5'
    },
    {
        'source': 'ru.gosuslugi.pgu.core.processing.exception.ProcessingServiceException: ru.gosuslugi.pgu.core.processing.exception.StopProcessingException: STOP_PROCESSINGHTTP 504 - Gateway Timeout. Invoke duration 95007',
        'target': 'ru.gosuslugi.pgu.core.processing.exception.ProcessingServiceException: ru.gosuslugi.pgu.core.processing.exception.StopProcessingException: STOP_PROCESSINGHTTP 504 - Gateway Timeout. Invoke duration 95007',
        'pseudo': 'Ошибка_6'
    },
    {
        'source': 'Smev3CallError{errorCode=ASYNCH_CALL_ERROR, message=\'SMEV-201:Некорректная информация о фтп вложениях; message id = 053e5428-713c-11ec-92a2-fe3963ee94b3\', category=\'null\', smevFault=null}',
        'target': 'Smev3CallError{errorCode=ASYNCH_CALL_ERROR, message=\'SMEV-201:Некорректная информация о фтп вложениях; message id = [[target]]\', category=\'null\', smevFault=null}',
        'pseudo': 'Ошибка_7'
    },
    {
        'source': 'Smev3CallError{errorCode=ASYNCH_CALL_ERROR, message=\'SMEV-201:Некорректная информация о фтп вложениях; message id = e1bb7bf4-7147-11ec-82c2-4e0a93826a11\', category=\'null\', smevFault=SmevFault{code=\'SMEVEncodedException\', description=\'SMEV-201:Некорректная информация о фтп вложениях; message id = e1bb7bf4-7147-11ec-82c2-4e0a93826a11\'}}',
        'target': 'Smev3CallError{errorCode=ASYNCH_CALL_ERROR, message=\'SMEV-201:Некорректная информация о фтп вложениях; message id = [[target]]\', category=\'null\', smevFault=SmevFault{code=\'SMEVEncodedException\', description=\'SMEV-201:Некорректная информация о фтп вложениях; message id = [[target]]\'}}',
        'pseudo': 'Ошибка_8'
    },
    {
        'source': 'Smev3CallError{errorCode=ASYNCH_CALL_ERROR, message=\'SMEV-403:Бизнес-данные сообщения не соответствуют схеме, зарегистрированной в СМЭВ. MessageId = 0558610d-716b-11ec-a7ae-12b068a68495: cvc-complex-type.2.4.a: Invalid content was found starting with element \'{"urn://egisso-ru/types/prsn-request/1.0.5":pdfInclude}\'. One of \'{"urn://egisso-ru/types/prsn-request/1.0.5":reportPeriod}\' is expected. [-1]\', category=\'null\', smevFault=null}',
        'target': 'Smev3CallError{errorCode=ASYNCH_CALL_ERROR, message=\'SMEV-403:Бизнес-данные сообщения не соответствуют схеме, зарегистрированной в СМЭВ. MessageId = [[target]]: cvc-complex-type.2.4.a: Invalid content was found starting with element \'{"urn://egisso-ru/types/prsn-request/1.0.5":pdfInclude}\'. One of \'{"urn://egisso-ru/types/prsn-request/1.0.5":reportPeriod}\' is expected. [-1]\', category=\'null\', smevFault=null}',
        'pseudo': 'Ошибка_9'
    },
    {
        'source': 'Smev3CallError{errorCode=REJECT, message=\'NO_DATA:Message processing error NDI2IFRyYW5zZmVyIGFib3J0ZWQuIERhdGEgY29ubmVjdGlvbiBjbG9zZWQK',
        'target': 'Smev3CallError{errorCode=REJECT, message=\'NO_DATA:Message processing error [[target]]',
        'pseudo': 'Ошибка_10'
    },
    {
        'source': 'Smev3CallError{errorCode=REJECT, message=\'UNKNOWN_REQUEST_DESCRIPTION:KVS03217 Вложенный документ не соответствует xsd-схеме (Обработка документа (id=00042d86-9a48-4e33-b60b-5cfe543f9d90, источник данных=EPGU, тип документа=VHC_20200101) не завершена. Причина: Валидация документа по XSD схеме не пройдена. Первая ошибка на строке 24 в колонке 7. Причина: cvc-complex-type.2.4.a: Invalid content was found starting with element \'From\'. One of \'{"http://pfrf.ru/fri/REGION/VEHICLE/1.2.0":Model}\' is expected.)\', category=\'null\', smevFault=null}',
        'target': 'Smev3CallError{errorCode=REJECT, message=\'UNKNOWN_REQUEST_DESCRIPTION:KVS03217 Вложенный документ не соответствует xsd-схеме (Обработка документа (id=[[target]], источник данных=EPGU, тип документа=VHC_20200101) не завершена. Причина: Валидация документа по XSD схеме не пройдена. Первая ошибка на строке 24 в колонке 7. Причина: cvc-complex-type.2.4.a: Invalid content was found starting with element \'From\'. One of \'{"http://pfrf.ru/fri/REGION/VEHICLE/1.2.0":Model}\' is expected.)\', category=\'null\', smevFault=null}',
        'pseudo': 'Ошибка_11'
    }
]
