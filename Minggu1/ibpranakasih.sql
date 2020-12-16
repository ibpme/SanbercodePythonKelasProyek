select albums.Title, artists.Name , tracks.Name
from albums 
inner join artists 
on albums.ArtistId = artists.ArtistId
join tracks 
on tracks.AlbumId = albums.AlbumId
where  artists.Name="Aerosmith" or (artists.Name ="AC/DC" and albums.Title = "Let There Be Rock");



