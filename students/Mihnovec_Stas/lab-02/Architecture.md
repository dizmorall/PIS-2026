# Архитектура Сервиса Жалоб (Complaint Service)

## Диаграмма Гексагональной Архитектуры

В основе сервиса лежит гексагональная архитектура (Ports and Adapters). Доменная логика полностью изолирована от внешнего мира.

```plantuml
@startuml
skinparam componentStyle rectangle

package "Infrastructure Layer (Адаптеры)" {
  [REST Controller] as RestApi
  [PostgreSQL Adapter] as DbAdapter
  [AI Service Client] as AIAdapter
}

package "Application Layer (Порты и Use-cases)" {
  interface "CreateComplaintUseCase" as PortIn
  interface "ComplaintRepository" as PortOutDB
  interface "AIModerationPort" as PortOutAI
  
  [ComplaintService] as AppService
}

package "Domain Layer (Ядро)" {
  [Complaint (Entity)] as ComplaintEntity
  [News (Entity)] as NewsEntity
}

' Входящие зависимости (Слева направо)
RestApi .down.> PortIn : "Вызывает"
PortIn <|-- AppService : "Реализует"

' Исходящие зависимости (Справа налево, DIP)
AppService .down.> PortOutDB : "Использует"
AppService .down.> PortOutAI : "Использует"
DbAdapter .up.|> PortOutDB : "Реализует"
AIAdapter .up.|> PortOutAI : "Реализует"

' Зависимости домена
AppService --> ComplaintEntity : "Оркестрирует"

note right of ComplaintEntity
  Домен не знает о БД, 
  REST API или внешних сервисах!
end note

@enduml