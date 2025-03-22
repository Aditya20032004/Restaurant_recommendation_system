# Restaurant_recommendation_system
# Restaurant_recommendation_system
 conda create -p venv python==3.12.7 -y
conda activate venv/
git remote -v
git pull origin main


pip install -r requirements.txt


## concept of Distiortion 
# eg.
there are n clusters with their respective centres
then formula=>
distortion for 1 = [distance(1,2)+distance(1,3)+........+distance(1,n)]/n

## concept of inertia
# eg. 
there are n clusters with their centre of clusters then 
inertia = (distance(1, centre))^2+(distance(2, centre))^2+(distance(3, centre))^2 # this is for each cluster
