
<?php 
class User_model extends CI_Model {
		public function __construct()
        {
                // Call the CI_Model constructor
                parent::__construct();
        }
		public function checkUser($user_name, $password){
			$this->db->select('count(id) as count');
			$this->db->where('user_name', $user_name);
			$this->db->where('password', $password);
			$this->db->where('is_active', true);
			$query = $this->db->get('users')->result();
			if ($query[0]->count > 0)
				return true;
			else
				return false;
		}
		public function getUserDetail($user_name){
			$result = $this->db->select('*')->from('users')->where('user_name', $user_name)->get()->result();
			return array(
				'user_id' => $result[0]->id,
				'user_name' => $result[0]->user_name,
				'display_name' => $result[0]->display_name,
				'user_role' => $result[0]->user_role
			);
		}
        /*public function get_last_ten_entries()
        {
                $query = $this->db->get('entries', 10);
                return $query->result();
        }

        public function insert_entry()
        {
                $this->title    = $_POST['title']; // please read the below note
                $this->content  = $_POST['content'];
                $this->date     = time();

                $this->db->insert('entries', $this);
        }

        public function update_entry()
        {
                $this->title    = $_POST['title'];
                $this->content  = $_POST['content'];
                $this->date     = time();

                $this->db->update('entries', $this, array('id' => $_POST['id']));
        }*/

}
