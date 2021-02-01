from django.shortcuts import render,redirect
from django.conf import settings
import os
import pandas as pd
import sqlite3
from sklearn.preprocessing import  StandardScaler
from sklearn.ensemble import GradientBoostingRegressor
from main.forms import add_prop_form

def predict(request):
    if request.method=="POST":
        form=add_prop_form(request.POST)
        if form.is_valid():
            p=form.save(commit=False)
            con = sqlite3.connect(os.path.join(settings.BASE_DIR, 'db.sqlite3'))
            df = pd.read_sql_query("SELECT distinct posted_by,under_construction,rera,rooms,room_type,area,ready_to_move,resale,location,loc_long,loc_lat,price from main_property", con)
            base_features = ['posted_by','under_construction','rera','rooms','room_type','area','loc_long','loc_lat']
            train_data = df[base_features]
            d = {'posted_by':[p.posted_by],'under_construction':[p.under_construction],'rera':[p.rera],'rooms':[p.rooms],'room_type':[p.room_type],'area':[p.area],'loc_long':[p.loc_long],'loc_lat':[p.loc_lat]}
            test_data= pd.DataFrame(data=d)
            y = df['price']
            cat_cols = [cname for cname in train_data.columns if  train_data[cname].dtype == "object"]
            Train_cat_colsOH = pd.get_dummies(train_data[cat_cols])
            pby=[0,0,0]
            rmt=[0,0]
            if p.posted_by=='Builder':
                pby[0]=1
            elif p.posted_by=='Dealer':
                pby[1]=1
            else:
                pby[2]=1
            if p.room_type=='BHK':
                rmt[0]=1
            else:
                rmt[1]=1
            testcol={'posted_by_Builder':[pby[0]],'posted_by_Dealer':[pby[1]],'posted_by_Owner':[pby[2]],'room_type_BHK':[rmt[0]],'room_type_RK':[rmt[1]]}
            Test_cat_colsOH= pd.DataFrame(data=testcol)
            print(Train_cat_colsOH)
            num_cols = [cname for cname in train_data.columns if train_data[cname].dtype in ['int64', 'float64']]
            scaler = StandardScaler()
            train_data[num_cols] = scaler.fit_transform(train_data[num_cols])
            test_data[num_cols] = scaler.transform(test_data[num_cols] )
            train_num_data = pd.DataFrame(train_data[num_cols])
            test_num_data = pd.DataFrame(test_data[num_cols])
            train_data =pd.concat([Train_cat_colsOH, train_num_data],axis=1)
            test_data =pd.concat([Test_cat_colsOH, test_num_data],axis=1)
            model =  GradientBoostingRegressor( max_depth=15, max_features='auto',
                            min_samples_split=6, n_estimators=200,
                            random_state=4)
            print(train_data.describe())
            print(test_data.describe())
            model.fit(train_data, y)
            print(test_data)
            SalesPrediction = model.predict(test_data)
            p.price=SalesPrediction[0]
            return render(request,'predict/showpred.html',{'p':p})
        else:
            print(form.errors)
    else:
        form=add_prop_form()
    return render(request,'predict/predict.html',{'form':form})