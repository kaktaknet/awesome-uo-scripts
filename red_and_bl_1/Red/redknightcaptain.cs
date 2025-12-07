using System;
using System.Collections;
using Server.Items;
using Server.Targeting;

namespace Server.Mobiles
{
	[CorpseName( "a knight's body" )]
	public class redknightcaptain : BaseCreature
	{
		public override bool ShowFameTitle{ get{ return false; } }
		
		[Constructable]
		public redknightcaptain() : base( AIType.AI_Melee, FightMode.Closest, 10, 1, 0.2, 0.4 )
		{			
			SpeechHue = Utility.RandomDyedHue(); 
			Name = "a red knight captain"; 
			Hue = Utility.RandomSkinHue(); 
			Body = 0x190; 

 	   		 // *Begin* //
   	   		Item plategloves = new PlateGloves();
      
         		plategloves.Hue = 2118;
        		 plategloves.Movable = false;

        		 AddItem( plategloves );
        		 // *End* //

 	   		 // *Begin* //
   	   		Item platearms = new PlateArms();
      
         		platearms.Hue = 2118;
        		 platearms.Movable = false;

        		 AddItem( platearms );
        		 // *End* //

 	   		 // *Begin* //
   	   		Item platehelm = new PlateHelm();
      
         		platehelm.Hue = 2118;
        		 platehelm.Movable = false;

        		 AddItem( platehelm );
        		 // *End* //

 	   		 // *Begin* //
   	   		Item platelegs = new PlateLegs();
      
         		platelegs.Hue = 2118;
        		 platelegs.Movable = false;

        		 AddItem( platelegs );
        		 // *End* //

 	   		 // *Begin* //
   	   		Item plategorget = new PlateGorget();
      
         		plategorget.Hue = 2118;
        		 plategorget.Movable = false;

        		 AddItem( plategorget );
        		 // *End* //

 	   		 // *Begin* //
   	   		Item platechest = new PlateChest();
      
         		platechest.Hue = 2118;
        		 platechest.Movable = false;

        		 AddItem( platechest );
        		 // *End* //

 	   		 // *Begin* //
   	   		Item broadsword = new Broadsword();
      
         		broadsword.Hue = 2118;
        		 broadsword.Movable = false;

        		 AddItem( broadsword );
        		 // *End* //  

 	   		 // *Begin* //
   	   		Item metalkiteshield = new MetalKiteShield();
      
         		metalkiteshield.Hue = 2118;
        		 metalkiteshield.Movable = false;

        		 AddItem( metalkiteshield );
        		 // *End* //  

 	   		 // *Begin* //
   	   		Item cloak = new Cloak();
      
         		cloak.Hue = 2118;
        		 cloak.Movable = false;

        		 AddItem( cloak );
        		 // *End* //  
          

          

          

			SetStr( 400, 500 );
			SetDex( 110, 150 );
			SetInt( 40, 50 );

			SetDamage( 15, 26 );

			SetSkill( SkillName.MagicResist, 90.0, 100.0 );
			SetSkill( SkillName.Swords, 110.0, 120.0 );
			SetSkill( SkillName.Tactics, 110.0, 120.0 );
			SetSkill( SkillName.Parry, 110.0, 120.0 );
			SetSkill( SkillName.Anatomy, 110.0, 120.0 );

			Fame = 10000;
			Karma = -1000;

			Item hair = new Item( Utility.RandomList( 0x203B, 0x2049, 0x2048, 0x204A ) );
			hair.Hue = Utility.RandomNondyedHue();
			hair.Layer = Layer.Hair;
			hair.Movable = false;
			AddItem( hair );

		

		}
	
		public override void GenerateLoot()
		{
			AddLoot( LootPack.FilthyRich );
		}

		public override bool AlwaysMurderer{ get{ return true; } }

		public redknightcaptain( Serial serial ) : base( serial )
		{
		}

		public override void Serialize( GenericWriter writer )
		{
			base.Serialize( writer );

			writer.Write( (int) 0 ); // version
		}

		public override void Deserialize( GenericReader reader )
		{
			base.Deserialize( reader );

			int version = reader.ReadInt();
		}
	}
}
