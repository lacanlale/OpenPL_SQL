-- CREATE OR REPLACE VIEW usa_athletes AS
-- SELECT 
-- 	amp.*
-- FROM athlete_meet_performances amp
-- LEFT JOIN meets ON meets.meet_id = amp.meet_id
-- WHERE meets.meet_country = 'USA';