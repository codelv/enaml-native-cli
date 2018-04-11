package {{cookiecutter.bundle_id}};

import android.view.View;
import android.widget.TextView;

import com.codelv.enamlnative.EnamlActivity;

public class MainActivity extends EnamlActivity {

    public View getLoadingScreen() {
        return findViewById(R.id.loadingView);
    }

    public TextView getMessageTextView() {
        return findViewById(R.id.textView);
    }
}
