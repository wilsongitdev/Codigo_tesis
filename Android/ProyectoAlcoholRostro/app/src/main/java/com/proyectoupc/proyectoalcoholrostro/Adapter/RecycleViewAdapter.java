package com.proyectoupc.proyectoalcoholrostro.Adapter;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.proyectoupc.proyectoalcoholrostro.R;
import com.proyectoupc.proyectoalcoholrostro.UserMeasure.User;
import com.squareup.picasso.Picasso;

import java.util.List;

public class RecycleViewAdapter extends RecyclerView.Adapter<RecycleViewAdapter.ViewHolder> {
    private List<User> mData;
    private LayoutInflater inflater;
    private Context context;
    final RecycleViewAdapter.OnItemClickListener listener;

    public interface OnItemClickListener{
        void OnItemClick(User item);

    }
    public RecycleViewAdapter(List<User> mData, Context context, RecycleViewAdapter.OnItemClickListener listener){
        this.mData = mData;
        this.inflater = LayoutInflater.from(context);
        this.context = context;
        this.listener = listener;
    }
    @Override
    public int getItemCount(){ return mData.size(); }

    @NonNull
    @Override
    public RecycleViewAdapter.ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = inflater.inflate(R.layout.view_rv_medalc, null);
        return new RecycleViewAdapter.ViewHolder(view);

    }

    @Override
    public void onBindViewHolder(@NonNull RecycleViewAdapter.ViewHolder holder, int position) {
        holder.bindData(mData.get(position));
    }

    public class ViewHolder extends RecyclerView.ViewHolder {
        ImageView iconimage;
        TextView fullname,ingalc , medalcmgl, medalcbac, date;
        ViewHolder(View itemview){
            super(itemview);
            ingalc = itemview.findViewById(R.id.ingAlc);
            fullname = itemview.findViewById(R.id.NameUserData);
            medalcmgl = itemview.findViewById(R.id.valAlcmgL);
            medalcbac = itemview.findViewById(R.id.valAlcBAC);
            date = itemview.findViewById(R.id.dateuserdata);
            iconimage =(ImageView) itemview.findViewById(R.id.imgperson);


        }
        void bindData(final User itemmed){
            fullname.setText(itemmed.getName()+" "+itemmed.getLastname());
            medalcmgl.setText(Double.toString(itemmed.getAlcoholmeasure().get(0).getAlcoholMgl()));
            medalcbac.setText(Double.toString(itemmed.getAlcoholmeasure().get(0).getAlcoholBAC()));

            String ing_alcohol = ((itemmed.getAlcoholmeasure().get(0).getIng_Alcohol() == true) ? "Sí" : "No");

            ingalc.setText(ing_alcohol);
            date.setText(itemmed.getAlcoholmeasure().get(0).getDate());
            //iconimage.set(itemmed.getFoto());
            Picasso.get().load(itemmed.getAlcoholmeasure().get(0).getUrlPicture()).into(iconimage);
            itemView.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    listener.OnItemClick(itemmed);
                }
            });
        }

    }
}
