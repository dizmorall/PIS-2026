-- Создаем материализованное представление (физически хранит результат запроса)
-- Идеально для дашборда "Топ подозрительных новостей"
CREATE MATERIALIZED VIEW top_suspicious_news AS
SELECT 
    news_url, 
    COUNT(id) as complaints_count, 
    MAX(ai_score) as highest_ai_score
FROM 
    complaints_read_model
WHERE 
    status = 'PENDING'
GROUP BY 
    news_url
HAVING 
    COUNT(id) > 5;

-- Создаем индекс для быстрого поиска
CREATE UNIQUE INDEX idx_top_suspicious_url ON top_suspicious_news (news_url);

-- Команда для фонового обновления (вызывается по CRON раз в 5 минут)
-- REFRESH MATERIALIZED VIEW CONCURRENTLY top_suspicious_news;